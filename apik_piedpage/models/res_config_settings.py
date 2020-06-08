# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class res_company(models.Model):
    _inherit = 'res.company'
    
    footer_note = fields.Text(string="Note sur pied de pièce", readonly=False, translate=True)
