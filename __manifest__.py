# -*- coding: utf-8 -*- 


{
    'name': 'Send Stock Delivery by email',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.1',
    'category': 'Inventory',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'data/mail_templates_data.xml',
        'views/stock_picking_views.xml'
    ],
    'license': 'LGPL-3',
}
