from odoo import fields, models, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    alt_ordered_qty = fields.Boolean(string='Qty Ordered')