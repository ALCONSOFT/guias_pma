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
    zafra = fields.Many2one('fincas_pma.zafras', string = '-Zafra [Año]', tracking=True)
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
    # 2021-01-06 - 10:50 - ALCE ,TRANSFERENCIA y ACARREO
    tipo_alce = fields.Char(string= '-Tipo_Alce', tracking=True)
    alce1 = fields.Char(string= '-Alce1', tracking=True)
    alce2 = fields.Char(string= '-Alce2', tracking=True)
    epl_alce1 = fields.Char(string= '-Empl. Alce1', tracking=True)
    epl_alce2 = fields.Char(string= '-Empl. Alce2', tracking=True)
    montacargas = fields.Char(string= '-Montacargas', tracking=True)
    epl_montacarga = fields.Char(string= '-Empl. Montacarga', tracking=True)
    tractor1 = fields.Char(string= '-Tractor 1', tracking=True)
    tractor2 = fields.Char(string= '-Tractor 2', tracking=True)
    epl_tractor1 = fields.Char(string= '-Empl. Tractor 1', tracking=True)
    epl_tractor2 = fields.Char(string= '-Empl. Tractor 2', tracking=True)
    nombre_tansportista = fields.Char(string= '-Nombre Transportista', tracking=True)
    num_epl_tansportista = fields.Char(string= '-Num. Empl. Transportista', tracking=True)
    neto_ton = fields.Float("-Neto [Tons C.]", tracking=True)
    ton1 = fields.Float("-Neto Caja 1[Tons]", tracking=True)
    ton2 = fields.Float("-Neto Caja 2[Tons]", tracking=True)
    cha1 = fields.Char(string= '-Chasis 1', tracking=True)
    tcha1 = fields.Char(string= '-Tara Chasis 1', tracking=True)
    cha2 = fields.Char(string= '-Chasis 2', tracking=True)
    tcha2 = fields.Char(string= '-Tara Chasis 2', tracking=True)
    mula = fields.Char(string= '-Mula', tracking=True)
    tmula = fields.Char(string= '-Tara Mula', tracking=True)
    chamula = fields.Char(string= '-Chasis Mula', tracking=True)
    tchamula = fields.Char(string= '-Tara Chasis Mula', tracking=True)
    caja1 = fields.Char(string= '-Caja 1', tracking=True)
    tcaja1 = fields.Char(string= '-Tara Caja 1', tracking=True)
    caja2 = fields.Char(string= '-Caja 2', tracking=True)
    tcaja2 = fields.Char(string= '-Tara Caja 2', tracking=True)
    promedio = fields.Float("-Promedio", tracking=True)
    dia_zafra = fields.Char("-Día Zafra ", tracking=True)
    detalle = fields.Char(string= '-Detalle', tracking=True)
    cerrado = fields.Boolean('-Cerrado', tracking=True)
    eliminado = fields.Boolean('-Eliminado', tracking=True)
    usuario_guia = fields.Char(string= '-Usuario Guía', tracking=True)
    procesado_contabilidad = fields.Boolean('-Procesado Contabilidad', tracking=True)
    hora_entrada = fields.Char('-Hora Entrada', tracking=True)
    hora_salida =  fields.Char('-Hora Salida', tracking=True)
    cerrado_total = fields.Boolean('-Cerrado Total', tracking=True)
    incetivo_tl = fields.Boolean('-Incentivo TL', tracking=True)
    incentivo_ti = fields.Boolean('-Incentivo TI', tracking=True)
    fecha_tiquete = fields.Char('-Fecha Tickete', tracking=True)
    hora_tiquete = fields.Char('-Hora Tickete', tracking=True)
    usuario_tiquete = fields.Char('-Usuario Tickete', tracking=True)
    origen_tiquete = fields.Char('-Origen Tickete', tracking=True)
    tipo_cane = fields.Selection([('PV','CAÑA PICADA VERDE'),('PQ','CAÑA PICADA QUEMADA'),('LV','CAÑA LARGA VERDE'),('LQ','CAÑA LARGA QUEMADA')], tracking=True)
    lote_hora = fields.Char('-Lote-Hora', tracking=True)
    # 2021-01-08 - 11:00
    cane = fields.Char('-Tipo Caña V/Q', tracking=True)
    neto_tonl = fields.Float("-Neto [Tons L.]", tracking=True)
    cant_cajas = fields.Integer(string="-Cant. Cajas", tracking=True)
    # 2021-01-09 - 04:15
    turno = fields.Char('-Turno', tracking=True)
    uplote = fields.Char(string='-UP.Lote', tracking=True, store=True, compute='_onchange_uplote', required=True)
    
    @api.depends('up','lote')
    def _onchange_uplote(self):
        lc_uplote = ''
        if not self.up:
            print('Sin UP', self.up)
            return lc_uplote
        else:
            self.uplote = self.up.code_up + '-' + self.lote
            lc_uplote = self.uplote
            print('Con UP:', lc_uplote)
        return lc_uplote    

class GuiasPurchase_OrderLine(models.Model):
    _inherit = 'purchase.order.line'

    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)
    # 2021-02-13: 14:25
    contrato = fields.Many2one('maintenance.equipment',string="Equipo Acarreo:", tracking=True, default='_mend')
    alce = fields.Many2one('maintenance.equipment',string="Equipo CyA:", tracking=True, default='_mend')
    caja = fields.Many2one('maintenance.equipment',string="Equipo Caja:", tracking=True, default='_mend')
    project_id = fields.Many2one('project.project',string="Project", default=1)

    @api.depends('up','lote')
    def _mend(self):
        query_str = 'SELECT id, name, external_id FROM public.maintenance_equipment where external_id='1001''
        self._cr.execute( query_str )
        meid = self._cr.fetchone()[0]
        return meid 

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

    class BitacoraAcarreo(models.Model):
    _name = 'guias_pma.bitacoraacarreo'
    _description = 'Bitacora de Acarreo'
    ########## A partir de la versión 13.0, un usuario puede iniciar sesión en varias empresas a la vez.
    #  Esto permite al usuario acceder a información de varias empresas, pero también crear / editar
    #  registros en un entorno de varias empresas.################
    _check_company_auto = True
    ##########################

    name = fields.Char('Nombre Evento', required=True)
    active = fields.Boolean('Activo', default=True)
    code_evento = fields.Char('Referencia Evento', required=True)
    description = fields.Text(string='Descripción')
    employee_in_charge = fields.Many2one('hr.employee', string='Empleado', tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    frente = fields.Many2one('fincas_pma.frentes', string = 'Frente', tracking=True)
    projects_id = fields.Many2one('project.project',string="Project")
    contrato = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    fechahora = fields.Datetime('Fecha Hora Cosecha', tracking=True)
    fecha = fields.Date('Fecha Cosecha', tracking=True, store=True)
    guia1 = fields.Char('N° Guia 1:', index=True, copy=False, default='0000000000')
    tickete1 = fields.Char('N° Tickete 1:', index=True, copy=False, default='000000')
    guia2 = fields.Char('N° Guia 2:', index=True, copy=False, default='0000000000')
    tickete2 = fields.Char('N° Tickete 2:', index=True, copy=False, default='000000') 