# -*- coding: utf-8 -*-
from odoo import models, fields, api
# HERENCIA - AMPLIANDO APLICACIONES EXISTENTES
#    AHORA AGREGAREMOS UNOS CAMPOS A UN MODELO EXISTENTE;  EN ESTE CASO SERIA EL MODELO
#    PROYECTO EL CAMPO A AGREGAR ES: fincas_pma EN EL NOMBRE DEL MODELO:
#    purchase.order ESTE SE BUSCA EN EL MENU: AJUSTES; OPCIN: TECNICO; SECCION:
#    SECUENCIA E IDENTIFICADRES
    
class GuiasPurchase_Order(models.Model):
    _inherit = 'purchase.order'
    
    
    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    ano = fields.Char('-Año', tracking=True)
    zafra = fields.Many2one('fincas_pma.zafras', string = '-Periodo Zafra [Año]', tracking=True)
    fechahoracaptura = fields.Datetime('-Fecha y Hora de Captura', tracking=True, default=fields.Datetime.now)
    fechahc = fields.Char('-Fecha Hora Captura en String', tracking=True)
    placa = fields.Char(string='-Placa', tracking=True)
    tipo_equipo = fields.Many2one('fincas_pma.tipo_equipo', string= '-Tipo de Equipo', tracking=True)
    frente = fields.Many2one('fincas_pma.frentes', string = '-Frente', tracking=True)
    up = fields.Many2one('fincas_pma.up', string = '-U.P.', tracking=True)
    lote = fields.Char('-LOT', tracking=True, default='000')
    tipo_vehiculo = fields.Char('-Tipo Vehículo', tracking=True)
    contrato = fields.Char(string= '-Contrato', tracking=True)
    fecha_guia = fields.Date('-Fecha Guía', tracking=True)
    fecha_quema = fields.Date('-Fecha Quema', tracking=True)
    hora_quema = fields.Char('-Hora Quema', tracking=True)
    # 2020-12-23 - 10:20
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)

class GuiasPurchase_OrderLine(models.Model):
    _inherit = 'purchase.order.line'

    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)

    #id|
    # name|                     <> '[MP-001] CAÑA DE AZUCAR'
    # sequence|                 <> 10
    # product_qty|              <> lbs -> Kg x1.0
    # product_uom_qty|          <> lbs -> Kg x1.0 
    # date_planned|
    # product_uom|              <> 1
    # product_id|               <> 2 - [MP-001]
    # price_unit|               <> 0.00
    # price_subtotal|           <> 0.00
    # price_total|              <> 0.00
    # price_tax|                <> 0.00
    # order_id|                 <> viene del encabezado!!!
    # account_analytic_id|
    # company_id|               <> 1
    # state|                    <> 'purchase'
    # qty_invoiced|     
    # qty_received_method|      <> 'stock_moves'
    # qty_received|             <?> 0.00
    # qty_received_manual|      <?> 0.00
    # qty_to_invoice|
    # partner_id|               <> Proveedor
    # currency_id|              <> 16 ??
    # display_type|
    # create_uid|
    # create_date|
    # write_uid|
    # write_date|
    # sale_order_id|
    # sale_line_id|