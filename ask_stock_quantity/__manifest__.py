# -*- coding: utf-8 -*-
{
    'name': "Stock Quantity",
    'summary': "Show Stock Quantity in Product Form View",

    'description': """
        This module adds a field to display the stock quantity of products directly in the product form view.
    """,

    'author': "Asksol",
    'website': "https://www.asksol.pk",
    'category': 'Sale',
    'version': '18.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock','sale_management'],

    # always loaded
    'data': [
        'views/stock_quantity_sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
}

