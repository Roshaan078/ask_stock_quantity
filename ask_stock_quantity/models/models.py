# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ask_stock_quantity(models.Model):
    _inherit = 'sale.order.line'

    qty_available = fields.Float(
        string="Quantity Available",
        related='product_id.qty_available',
        store=False,
        readonly=True
    )