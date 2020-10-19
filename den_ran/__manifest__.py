# -*- coding: utf-8 -*-

{
    "name": "Adaptations DeN-RAN",
    "version": "1.0",
    "author": "APIK CONSEILS - Jean-Noël ETIENNE",
    "website": "http://www.apik-conseils.com",
    "license": "AGPL-3",
    "category": "Vertical",
    "description": "Module complémentaire Den-Ran",
    "depends": [
        'base',
        'account',
        'product',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/group.xml',
        'views/res_users.xml',
        'views/res_users_address.xml',
        'report/report.xml',
        'report/report_product_product_templates.xml',
        'wizard/nbetiquettes.xml',
        'report/report_saleorder.xml',
        'report/report_purchaseorder.xml',
        'report/report_purchasequotation.xml',
        'report/report_invoice.xml',
        'report/report_deliveryslip.xml',
    ],
    "demo": [

    ],
    'qweb': [],
    'installable': True,
    'application':True,
}
