# -*- coding: utf-8 -*-
# Part of Odoo. See LICENCE file for full copyright and licensing details.
{
    'name': 'Profile B.P. Logistics',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Custom',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customisations for B.P. Logistics',
    'version': '1.1',
    'description': """
    """,
    'depends': [
        'sale',
        'sale_management',
        'account',
        'stock',
        'mail'
    ],
    'data': [
        'views/product_template_view_ext.xml',
        'views/stock_move_line_view_ext.xml',
        'views/stock_picking_view_ext.xml',

        'report/report_deliveryslip.xml',

        'security/group_security.xml',
        'security/ir.model.access.csv',
    ],
    'sequence': 666,
    'installable': True,
    'application': False,
}
