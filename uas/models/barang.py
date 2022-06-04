from odoo import models, fields, api, _
from odoo.exceptions import UserError

class barang(models.Model):  # inherit dari Model
    _name = 'uas.barang'  # atribut dari class Model
    _description = 'class untuk barang'
    # rec_name = 'name'

    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    id_barang = fields.Char('id_barang', size=64, required=True, index=True, readonly=True,default='new',
                       states={})


    nama_barang = fields.Char('nama_barang', size=64, required=True, index=True, readonly=False,
                       states={'draft': [('readonly', False)]})

    ukuran = fields.Char('ukuran', size=64, required=True, index=True, readonly=False,
                        states={'draft': [('readonly', False)]})

    warna = fields.Char('warna', size=64, required=True, index=True, readonly=False,
                           states={'draft': [('readonly', False)]})

    qty_dus = fields.Char('qty_dus', size=64, required=True, index=True, readonly=False,
                        states={'draft': [('readonly', False)]})

    qty_pcs = fields.Char('qty_pcs', size=64, required=True, index=True, readonly=False,
                        states={'draft': [('readonly', False)]})

    harga = fields.Char('harga', size=64, required=True, index=True, readonly=False,
                          states={'draft': [('readonly', False)]})

    disc = fields.Char('disc', size=64, required=True, index=True, readonly=False,
                          states={'draft': [('readonly', False)]})
    stok_barang = fields.Char('stok_barang', size=64, required=True, index=True, readonly=False,
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



    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'
