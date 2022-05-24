from odoo import models, fields, api, _
from odoo.exceptions import UserError

class buku(models.Model):  # inherit dari Model
    _name = 'library.buku'  # atribut dari class Model
    _description = 'class untuk buku'
    # rec_name = 'name'

    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    id_buku = fields.Char('id_buku', size=64, required=True, index=True, readonly=True,default='new',
                       states={})


    judul = fields.Char('judul_buku', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})

    penerbit = fields.Char('penerbit', size=64, required=True, index=True, readonly=False,
                        states={'draft': [('readonly', False)]})

    harga = fields.Char('harga sewa', size=64, required=True, index=True, readonly=False,
                           states={'draft': [('readonly', False)]})

    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')


    confirm_partner_id = fields.Many2one('res.partner', 'Confirm By', readonly=True)
    # Ketambahan voting_ids supaya bs ambil dari votings.py, s -> ditambahin karena penamaan default di odoo 1:M
    transaksi_ids = fields.One2many('library.transaksi', 'buku_id', string='transaksi')

    total_pinjam = fields.Integer("Pinjam", compute="_compute_vote", store=True, default=0)
    total_kembali = fields.Integer("Kembali", compute="_compute_vote", store=True, default=0)

    _sql_constraints = [('id_buku_unik', 'unique(id_buku)', _('buku must be unique!'))]

    @api.depends("transaksi_ids", "transaksi_ids.vote", "transaksi_ids.state")


    def _compute_vote(self):
        for buku in self.filtered(lambda s: s.state == "done"):
            val = {
                "total_pinjam": 0,
                "total_kembali": 0,

            }
            for rec in buku.transaksi_ids.filtered(lambda s: s.state == "voted"):
                # lambda merupakan on the fly function dari phyton
                # s ini adalah self dari voting_ids, fungsi filtered ini akan memfilter khusus state yang bernilai voted
                # bisa pake looping, ga ush difilter. Tapi pengecekan tidak efisien
                # karena misal ada 100 data, trs hanya 2 yang canceled berarti tetep 100 pengecekan. Sedangkan filter hanya 2x saja
                if rec.vote == "Pinjam":
                    val["total_pinjam"] += 1

                elif rec.vote == "Kembali":
                    val["total_kembali"] += 1

            for rec in buku.transaksi_ids.pengembalian_ids.filtered(lambda ss: ss.state == "voted"):
                if rec.vote == "Pinjam":
                    val["total_pinjam"] += 1

                elif rec.vote == "Kembali":
                    val["total_kembali"] += 1


            buku.update(val)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'
        if self.id_buku == 'new' or not self.id_buku:
            seq = self.env['ir.sequence'].search([("code", "=", "library.buku")])
            if not seq:
                raise UserError(_("library.buku sequence not found, please create library.buku sequence"))
            self.id_buku = seq.next_by_id()

    def action_settodraft(self):
        self.state = 'draft'
