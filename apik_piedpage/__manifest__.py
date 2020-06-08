# -*- coding: utf-8 -*-

{
    "name": "Apik - piedpage",
    "version": "1.0",
    "author": "APIK CONSEILS - Michel GUIHENEUF",
    "website": "http://www.apik-conseils.com",
    "license": "AGPL-3",
    "category": "Vertical",
    "description": "Apik - Pied de page",
    "depends": [
        'base',
        
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/apik_res_company_views.xml',
        #'report/apik_report_templates.xml',
    ],
    "demo": [
	],
    'qweb': [
    ],
    'installable': True,
	'application':True,
}
