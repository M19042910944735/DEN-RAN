# -*- coding: utf-8 -*-
{
    'name': "Quadra Export ASCII",

    'summary': """
        This module allow to export account move lines in an ASCII format accepted by Quadratus.
    """,

    "author": "Auneor Conseil",
    "website": "http://www.auneor-conseil.fr",

    'category': 'Accounting',
    'version': '0.1',
    'price': 50,
    'currency': "EUR",


    'depends': [
        'account',
    ],

    'data': [
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',

        'wizard/export_ascii_views.xml',
   ],
     "license":  "Other proprietary",
}
