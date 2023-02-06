from odoo import fields, models
from odoo.addons import decimal_precision as dp


class StockMove(models.Model):
    _inherit = 'stock.move'

    alt_ordered_qty = fields.Float(string='Qty Ordered', digits=dp.get_precision('Product Unit of Measure'), default=0.0)

    picking_type_code = fields.Selection([
        ('incoming', 'Vendors'),
        ('outgoing', 'Customers'),
        ('internal', 'Internal')], related='picking_id.picking_type_id.code',
        readonly=True)
