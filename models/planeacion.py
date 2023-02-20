# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp import exceptions
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class Planning_log (models.Model):
    _name = 'guias_pma.planning_log'
    _description = 'Planeacion por Proyecto - UP+Lote'
    _check_company_auto = True
    ############################
    name = fields.Char('Nombre Tarea', required=False)
    active = fields.Boolean('Activo', default=True)
    code_estatus = fields.Many2one('guias_pma.estatus', string='Estatus', default=5, trackig=True)
    ano = fields.Char('Año', tracking=True)
    zafra = fields.Many2one('fincas_pma.zafras', string = '-Zafra [Año]', tracking=True)
    dia_zafra = fields.Char("Día Zafra ", tracking=True)
    turno = fields.Selection([('D','Diurno'),('N','Nocturno')],string='Turno', tracking=True)
    lote_hora_inicial = fields.Char('Lote Hora Ini.', tracking=True)
    lote_hora_final = fields.Char('Lote Hora Fin.', tracking=True)
    horas_estimadas = fields.Float('Hrs Estim.', tracking=True, required=True)
    qty_acarreo_estimated = fields.Float("Cant. Acarreo Est. [Tons. Cortas]", tracking=True)
    qty_acarreo_estimated_max = fields.Float("Cant. Acarreo Est. Max.[Tons. Cortas]", tracking=True)
    qty_acarreo_estimated_min = fields.Float("Cant. Acarreo Est. Min.[Tons. Cortas]", tracking=True)
    qty_almacen_estimated = fields.Float("Cant. Almacen Est. (x Hr.)[Tons. Cortas]", tracking=True)
    description = fields.Text(string='Descripción', trackig=True)
    company_id = fields.Many2one('res.company', store=True, readonly=False, default=lambda self: self.env.company, required=True)
    employee_in_charge = fields.Many2one('hr.employee', string='Empleado', tracking=True)
    frente = fields.Many2one('fincas_pma.frentes', string = 'Frente', tracking=True)
    finca = fields.Many2one('fincas_pma.fincas', string = 'Finca', tracking=True)
    projects_id = fields.Many2one('project.project',string="Project", default=1, trackig=True)
    