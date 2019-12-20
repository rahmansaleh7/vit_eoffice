# -*- coding: utf-8 -*-
{
    'name': "vit_eoffice",

    'summary': """
        Addon Terbaik untuk kebutuhan kantor anda""",

    'description': """
        Ini adalah addon untuk keperluan kantor
    """,

    'author': "Iqbal A",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Office',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/surat.xml',
        'views/klasifikasisurat.xml',
        'views/templatesurat.xml',
        'views/user.xml',
        'data/sequence.xml',
        'report/surat.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}