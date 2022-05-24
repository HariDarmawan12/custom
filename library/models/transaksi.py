from odoo import models, fields, api, _

class transaksi(models.Model):  # inherit dari Model
    _name = 'library.transaksi'  # atribut dari class Model
    _description = 'class untuk transaksi'
    #rec_name = 'name'
    #_order = 'date desc'
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    id_transaksi = fields.Char('id_transaksi', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})


    #name = fields.Char('name', size=64, required=True, index=True, readonly=False,
                       #states={'draft': [('readonly', False)]})




    datepinjam = fields.Date('Tanggal pinjam ', default=fields.Date.context_today, readonly=True,
                             states={'draft': [('readonly', False)]})
    datekembali = fields.Date('Tanggal kembali ', default=fields.Date.context_today, readonly=True,
                              states={'draft': [('readonly', False)]})  # real
    dateline = fields.Date('dateline', default=fields.Date.context_today, readonly=True,
                               states={'draft': [('readonly', False)]})
    denda = fields.Integer("Denda", compute="_compute_denda", store=True, default=0)

    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('voted', 'Voted'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=False,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states



    vote = fields.Selection([('Pinjam','Pinjam'),
                             ('Kembali','Kembali')], 'vote', required=True,readonly=False)

    transaksi_id = fields.Many2one('res.users', 'voted by', readonly=True, ondelete='cascade',
                               default=lambda self: self.env.user)

    buku_id = fields.Many2one('library.buku', string='buku', readonly=True, ondelete="cascade",
                               states={'draft': [('readonly', False)]})

    mhs_id = fields.Many2one('library.mhs', string='mhs', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]})

    pengembalian_ids = fields.One2many('library.pengembalian', 'transaksi_id', string='pengembalian')

    #sponsor_ids = fields.Many2many('res.partner', 'ideaa_ideaa_res_partner_rel', 'ideaa_ideaa_id', 'res_partner_id', 'Sponsors')
    #sponsor_ids = fields.Many2many('res.partner', string='Sponsors')

    _sql_constraints = [('id_transaksi_unik', 'unique(id_transaksi)', ('transaksi must be unique!'))]

    @api.depends('datekembali', 'dateline')
    def _compute_denda(self):
        if self.dateline and self.datekembali:
            dateline = fields.Datetime.from_string(self.dateline)
            datekembali = fields.Datetime.from_string(self.datekembali)
            if self.datekembali > self.dateline:
                self.denda = abs((datekembali - dateline).days) * (7000)
            if self.datekembali < self.dateline:
                self.denda = 0

    def action_canceled(self):
        self.state = 'canceled'
    def action_vote(self):
        self.state = 'voted'
    def action_settodraft(self):
        self.state = 'draft'

    def tes_bookrent(self):
        print("ini di bookrent")
        t = self.enc.context.get("keterangan")
        print(t)


