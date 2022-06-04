{
    'name': 'uas',  #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Hari',
    'summary': 'Modul uas SIB UK Petra', #deskripsi singkat dari modul
    'description': 'uas management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di ideaa/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'],  # list of dependencies, conditioning startup order
    'data': [
        'views/barang_views.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [],  #untuk memberi tahu static file, misal CSS
    'demo': [],  #demo data (for unit tests)
    'installable': True,
    'auto_install': False,  # indikasi install, saat buat database baru
}
