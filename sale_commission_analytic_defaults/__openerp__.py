# -*- encoding: utf-8 -*-

{
    'name': 'Sale Commission Analytic Defaults',
    'author': 'Viktor Anikeenko <lolooksdffff@gmail.com>',
    'category': 'Generic Modules/Sales & Purchases',
    'summary': 'Default agents for Analytic Account',
    'depends': [
        'account',
        'sale',
        'sale_commission',
    ],
    'data': [
        'views/account_analytic_account_view.xml',
        'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
}
