from odoo import fields, models
from odoo.addons import decimal_precision as dp


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    alt_ordered_qty = fields.Float(string='Qty Ordered', digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    is_picking_alt_ordered_qty = fields.Boolean(related='move_id.picking_id.alt_ordered_qty')


    def _get_aggregated_product_quantities(self, **kwargs):
        """Returns dictionary of products and corresponding values of interest + hs_code

        Unfortunately because we are working with aggregated data, we have to loop through the
        aggregation to add more values to each datum. This extension adds on the hs_code value.

        returns: dictionary {same_key_as_super: {same_values_as_super, hs_code}, ...}
        """
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for aggregated_move_line in aggregated_move_lines:
            source_location = self.move_id.location_id.display_name
            aggregated_move_lines[aggregated_move_line]['source_location'] = source_location
        return aggregated_move_lines
