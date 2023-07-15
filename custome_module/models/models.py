from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float('Qty Available',related="product_id.qty_available")

    def last_po_view(self):
        if self.product_id:
            po_line_id = self.env['purchase.order.line'].search([('product_id', '=', self.product_id.id)]).mapped('order_id')
            if po_line_id:
                action = {
                    'name': _('Last Purchase Order'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'purchase.order',
                    'view_mode': 'tree,form',
                    'domain': [('id','=', po_line_id.ids[0])],
                    'res_id': po_line_id.ids[0]
                }
                return action
            else:
                raise ValidationError(_('There is No Purchase order for this product'))