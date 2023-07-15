# -*- coding: utf-8 -*-
{
    'name': "custome_module",

    'summary': """""",

    'description': """""",

    'author': "My Company",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'stock'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
  }
