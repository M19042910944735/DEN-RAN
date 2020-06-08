# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError
from datetime import datetime, timedelta, date
logger = logging.getLogger(__name__)



class res_users(models.Model):
    _inherit = "res.users"

    adresse_id = fields.Many2one('res.users.address', string="Adresse")
