{
    'name': 'Library',  #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Hari',
    'summary': 'Modul library SIB UK Petra', #deskripsi singkat dari modul
    'description': 'Ideas management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di ideaa/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'],  # list of dependencies, conditioning startup order
    'data': [
        'security/ir.model.access.csv',
        'views/buku_views.xml',
        'views/transaksi_views.xml',
        'views/mhs_views.xml',
        'views/pengembalian_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'qweb': [],  #untuk memberi tahu static file, misal CSS
    'demo': [],  #demo data (for unit tests)
    'installable': True,
    'auto_install': False,  # indikasi install, saat buat database baru
}

