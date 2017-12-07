# -*- coding: utf-8 -*-
{
    'name': "Product Multi Barcodes",

    'summary': """This module allows you to assign multi barcodes on a product.
        """,

    'description': """
        
    """,

    'author': "Abdelmalik Yousif",
    'sequence': 1,
    'website': "",
    'category': 'Generic Modules',
    'version': '1.0',
    'currency': 'EUR',
    'price': 35.0,
    'depends': ['point_of_sale', 'stock'],


    'data': [
        'views/malik.xml',
        'views/malik_v.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],

    'demo': [
        #'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
