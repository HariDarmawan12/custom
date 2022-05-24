from odoo import models, fields, api, _

class mhs(models.Model):  # inherit dari Model
    _name = 'library.mhs'  # atribut dari class Model
    _description = 'class untuk mhs'
    #rec_name = 'name'
    #_order = 'date desc'
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    id_mhs = fields.Char('id_mhs', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})


    name = fields.Char('name', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})

    state = fields.Selection(
        [('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
         ('voted', 'Voted'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=False,  # krn required, sebaiknya dikasi default
        default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states

    #transaksi_ids = fields.One2many('library.transaksi', 'mhs_id', string='transaksi')




    #mhs_id = fields.Many2one('res.users', 'voted by', readonly=True, ondelete='cascade',
                               #default=lambda self: self.env.user)

    buku_id = fields.Many2one('library.buku', string='buku', readonly=True, ondelete="cascade",
                               states={'draft': [('readonly', False)]},
                               domain="[('state', '=', 'done'), ('active', '=', 'True')]")


    #sponsor_ids = fields.Many2many('res.partner', 'ideaa_ideaa_res_partner_rel', 'ideaa_ideaa_id', 'res_partner_id', 'Sponsors')
    #sponsor_ids = fields.Many2many('res.partner', string='Sponsors')

    _sql_constraints = [('id_mhs_unik', 'unique(id_mhs)', ('Ideas must be unique!'))]

    def action_canceled(self):
        self.state = 'canceled'
    def action_vote(self):
        self.state = 'voted'
    def action_settodraft(self):
        self.state = 'draft'
