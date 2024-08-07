# -*- coding: utf-8 -*-
{
    'name': "KEDATECH",

    'summary': """
        Skill Test""",

    'description': """
        Odoo technical test
    """,

    'sequence': 0,
    'author': "Felis Tigris Hafizhulloh",
    'website': "https://www.keda-tech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material.xml',
        'views/supplier.xml',
        'views/main_menu.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'installable': True,
    'application': True,
    'auto_install': False,
}