# -*- coding: utf-8 -*-
{
    'name': "method_cierre_pos_forzar",

    'summary': """
        Cierre sessión del pos sin contabilización""",

    'description': """
        Con el objetivo de facilitar la operación a los usuario del POS que
        no utilizan contabilidad ya que con este cierre no se contabilizan los movimientos
    """,

    'author': "Method ERP",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}