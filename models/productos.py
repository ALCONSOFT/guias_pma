# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp import exceptions
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
#from odoo.exceptions import AccessError, UserError, ValidationError
# HERENCIA - AMPLIANDO APLICACIONES EXISTENTES
#    AHORA AGREGAREMOS UNOS CAMPOS A UN MODELO EXISTENTE;  EN ESTE CASO SERIA EL MODELO
#    PROYECTO EL CAMPO A AGREGAR ES: fincas_pma EN EL NOMBRE DEL MODELO:
#    purchase.order ESTE SE BUSCA EN EL MENU: AJUSTES; OPCIN: TECNICO; SECCION:
#    SECUENCIA E IDENTIFICADRES
class ProductTemplateGuias(models.Model):
    _inherit = "product.template"

    _sql_constraints = [
        ('default_code',
         'UNIQUE(default_code)',
         "El código default debe ser único"),

        ('name_unique',
         'UNIQUE(name)',
         "El nombre del producto debe ser único"),
    ]    
     
