# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class StockOverProcessedTransfer(models.TransientModel):
    _inherit = 'stock.overprocessed.transfer'

    date_done = fields.Datetime(string="Date")

    @api.model
    def default_get(self, fields_list):
        res = super(StockOverProcessedTransfer, self).default_get(fields_list)
        res["date_done"] = self.env.context.get("force_period_date", fields.Datetime.now())
        return res

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        return self.picking_id.with_context(skip_overprocessed_check=True, force_period_date=self.date_done).button_validate()
