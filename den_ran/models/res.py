# -*- coding: utf-8 -*-
# WARNING: STOP APPELER LES FICHIERS "FICHIER" SVP

from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError
from datetime import datetime, timedelta, date
logger = logging.getLogger(__name__)


class res_users_address(models.Model):
    _name = "res.users.address"
    _description = "modèle d'adresse pour les res.users"


    name = fields.Char('Nom', required=True)
    description = fields.Char('Description')
    street = fields.Char('Rue')
    street_2 = fields.Char('Rue 2')
    city = fields.Char('Ville')
    zip = fields.Char('Code postal')
    country_id = fields.Many2one('res.country', "Pays", default=lambda self: self.env.ref('base.fr').id)
    website = fields.Char('Site web')
    phone = fields.Char('Téléphone')
    mobile = fields.Char('Mobile')
    email = fields.Char('Adresse e-mail', default=lambda self: self.env.user.login)


class res_partner(models.Model):
    _inherit = "res.partner"

    client_quadra = fields.Char('Cpt Quadra Clt')
    fourn_quadra = fields.Char('Cpt Quadra Fourn')
