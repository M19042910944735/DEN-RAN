# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
import logging
logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def calculer_prix_ttc(self,product=False):
        
        prix_calcule = product.taxes_id.compute_all(product.lst_price)
        prix_ttc = round(prix_calcule['total_included'],2)

        return prix_ttc




