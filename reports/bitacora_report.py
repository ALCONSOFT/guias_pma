# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Please note that these reports are not multi-currency !!!
#

import re

from odoo import api, fields, models, tools
from odoo.exceptions import UserError
from odoo.osv.expression import expression


class bitacora_report(models.Model):
    _name = "guias_pma.bitacora_report"
    _description = "Bitacora Report"
    _auto = False
    _order = 'date_order desc'

    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    code_estatus = fields.Many2one('guias_pma.estatus', string='Estatus', default=5, trackig=True)
    partner_id = fields.Many2one('res.partner', 'Vendor', readonly=True)
    product_qty = fields.Float(string='Peso M.E.', digits='Product Unit of Measure', required=True)
    projects_id = fields.Many2one('project.project',string="Project", default=1, trackig=True)
    contrato = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    guia1 = fields.Char('N° Guia 1:', index=True, copy=False, default='0000000000', trackig=True)
    tickete1 = fields.Char('N° Tickete 1:', index=True, copy=False, default='000000', trackig=True)
    fechahora_sal_fre = fields.Datetime('Fecha Hora Sal. Fre.', tracking=True,default=fields.Datetime.now)
    fechahora_lle_pes = fields.Datetime('Fecha Hora Lle. Pes.', tracking=True)
    fechahora_pesado = fields.Datetime('Fecha Hora Pesado', tracking=True)
    fechahora_des_pat = fields.Datetime('Fecha Hora des. Pat.', tracking=True)
    fechahora_ret_fre = fields.Datetime('Fecha Hora Ret. Fre.', tracking=True)
    dia_zafra = fields.Char("-Día Zafra ", tracking=True)
    lote_hora = fields.Char('-Lote-Hora', tracking=True)
    name = fields.Char('Nombre Order ID', required=False)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    fechahoracaptura = fields.Datetime('-Fecha y Hora de Captura', tracking=True, default=fields.Datetime.now)
    uplote = fields.Many2one('project.project',string="Project", default=1, trackig=True)
    equipo = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    alce = fields.Many2one('maintenance.equipment',string="Equipo CyA:", tracking=True, default=1)
    neto_ton = fields.Float("-Neto [Tons C.]", tracking=True)
    equipo_cya = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    frente = fields.Many2one('fincas_pma.frentes', string = 'Frente', tracking=True)

    def init(self):
        # self._table = bitacora_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM ( %s )
            %s
            )""" % (self._table, self._select(), self._from(), self._group_by()))

    def _select(self):
        select_str = """SELECT 
        bit.id,
        bit.code_estatus,
        bit.projects_id,
        bit.contrato,
        bit.guia1,
        bit.tickete1,
        bit.fechahora_sal_fre,
        bit.fechahora_lle_pes,
        bit.fechahora_pesado,
        bit.fechahora_des_pat,
        bit.fechahora_ret_fre,
        po.partner_id,
        po.dia_zafra ,
        po.lote_hora ,
        po."name" ,
        po.secuencia_guia ,
        po.fechahoracaptura ,
        po.frente ,
        pol.project_id as UpLote,
        pol.contrato as equipo,
        pol.alce ,
        pol.product_id,
        sum(pol.product_qty) as neto_ton,
        me.name as equipo_cya
        """
        return select_str

    def _from(self):
        from_str = """
        guias_pma_bitacoraaca_col bit left join purchase_order po
        on bit.tickete1 = po.origin 
        left join purchase_order_line pol 
        on pol.order_id = po.id
        left join maintenance_equipment me 
        on pol.alce = me.id
        """
        return from_str

    def _group_by(self):
        group_by_str = """GROUP BY
        bit.id,
        bit.code_estatus ,
        bit.projects_id,
        bit.contrato,
        bit.guia1,
        bit.tickete1,
        bit.fechahora_sal_fre,
        bit.fechahora_lle_pes,
        bit.fechahora_pesado,
        bit.fechahora_des_pat,
        bit.fechahora_ret_fre,
        po.partner_id,
        po.dia_zafra ,
        po.lote_hora ,
        po."name" ,
        po.secuencia_guia ,
        po.fechahoracaptura ,
        po.frente ,
        pol.project_id ,
        pol.product_id,
        pol.contrato ,
        pol.alce ,
        me.name 
        """
        return group_by_str