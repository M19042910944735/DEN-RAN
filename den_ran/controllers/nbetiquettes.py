# -*- coding: utf-8 -*-

from openerp import models, fields, api
from werkzeug.wrappers import Response
from openerp import http, SUPERUSER_ID
from openerp.http import request
import logging
import urllib
import base64
import datetime
import io
import csv
logger = logging.getLogger(__name__)


class impr_etiquettes(http.Controller):
    _name="product.template"
    
    @http.route("/nb_etiquettes/<int:product_id>", type='http', auth="user")
    def imprimer_etiquettes(self, product_id, **args):
        #logger.info("impr_etiquette_controller")

        nbetiquettes_obj = request.env['wizard.nb_etiquettes']
        nbetiquettes = nbetiquettes_obj.sudo().search([('id', '=', product_id)])

        produit = nbetiquettes.produit
        nb = nbetiquettes._get_nb_etiquettes()
                 
        #
        # on génére le fichier étiquette selon l'opération
        #  
        liste_etiq = []
        i = 0
        while i < nb:
            liste_etiq.extend(produit.ids)
            i = i + 1

        liste_etiq.sort()

        pdf_etiq = request.env.ref('den_ran.etiquette_articles').sudo().render_qweb_pdf(liste_etiq)[0]
        encoded_string = base64.b64encode(pdf_etiq)

        response = Response()
        response.data = pdf_etiq
        response.headers.add('content-disposition','attachment;filename="etiquettes.pdf"')

        return response





