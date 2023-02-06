{
    'name': 'B.P. Logistics Stock',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Inventory',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customisations for B.P. Logistics',
    "version": "15.0.1.0.0",
    'description': """
    """,
    'depends': [
        'sale',
        'account',
        'sale_stock',
        'mail',
        'product_expiry'
    ],
    'data': [
        'views/product_template_view_ext.xml',
        'views/stock_picking_view_ext.xml',
        'views/stock_move_line_views.xml',
        'report/report_deliveryslip.xml',

        'security/group_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
