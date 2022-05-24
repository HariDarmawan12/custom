from odoo import models, fields, api
#_ untuk translate

class mhs(models.Model): #inherit dari Model -> ini nama class sesuai python
    _name = 'nilai.mhs' #attribut dari class Model (lihat dokumen odoo) Modul.Model  jadi nama tabel
    # (ini nama class/tabel sesuai odoo), jadi kalau akses data berdasarkan nama ini
    _description = 'class untuk mhs'
    #_rec_name = 'name' #default-nya name, ini untuk memberi tahu field mana yang jadi rec_name.
    #_order = 'date desc' #defaultnya adalah id, pengaruhnya saat list view


    name = fields.Char('mhs', size=10, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})


    nrp = fields.Char('nrp', size=60, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})

    status = fields.Char('status', size=60, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})

    tes = fields.Char('tes', size=10, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})