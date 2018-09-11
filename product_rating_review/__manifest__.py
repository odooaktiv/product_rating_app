# -*- coding: utf-8 -*-

{
    'name': 'Product Rating',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Product Rating & Review at Backend',
    'description': """
Features
=============
This specific module allows you manage ratings and reviews of website
products at Odoo backend.
    """,
    'category': 'Product',
    'author': 'Aktiv Software',
    'depends': [
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
    ],

    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
}
