# -*- coding: utf-8 -*-

from odoo import models, fields, api
from math import *
import logging
logger = logging.getLogger(__name__)

class wizard_nb_etiquettes(models.TransientModel):
    _name = "wizard.nb_etiquettes"

    def _get_active_product_id(self):
        product_obj = self.env['product.template']
        product_id = self.env.context.get('active_ids')

        return product_obj.browse(product_id)

    def _get_nb_etiquettes(self):
        nb = self.nbetiq
        return nb

    produit = fields.Many2many('product.template',string='Produit', default=_get_active_product_id)
    nbetiq = fields.Integer("Nombre d'étiquettes",default="1")

    @api.multi
    def imprimer_etiquettes(self,**args):
 
        liste_produit = []
  
        for x in self.produit:

            liste_produit.append(x.ids)
 
        return {
                'type': 'ir.actions.act_url',
                'res_model' : 'product.template',
                'produit' : liste_produit,
                'url': "/nb_etiquettes/" + str(self.id),
                'target': 'new',
                }

 
