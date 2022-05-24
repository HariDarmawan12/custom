from odoo import models, fields, api, _

class pengembalian(models.Model):  # inherit dari Model
    _name = 'library.pengembalian'  # atribut dari class Model
    _description = 'class untuk transaksi'
    #rec_name = 'name'
    #_order = 'date desc'
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field



    id_pengembalian = fields.Char('id_pengembalian', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})

    date = fields.Date('Tanggal kembali', default=fields.Date.context_today, readonly=True)




    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('voted', 'Voted'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=False,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states



    vote = fields.Selection([('Pinjam','Pinjam'),
                             ('Kembali','Kembali')], 'vote', required=True,readonly=False)



    transaksi_id = fields.Many2one('library.transaksi', string='transaksi', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]})

    buku_id = fields.Many2one('library.buku', string='buku', readonly=True, ondelete="cascade",
                              states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'), ('active', '=', 'True')]")



    #sponsor_ids = fields.Many2many('res.partner', 'ideaa_ideaa_res_partner_rel', 'ideaa_ideaa_id', 'res_partner_id', 'Sponsors')
    #sponsor_ids = fields.Many2many('res.partner', string='Sponsors')

    _sql_constraints = [('name_unik', 'unique(name)', ('Ideas must be unique!'))]

    def action_canceled(self):
        self.state = 'canceled'
    def action_vote(self):
        self.state = 'voted'
    def action_settodraft(self):
        self.state = 'draft'
