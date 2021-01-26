# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv.expression import AND


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def sale_in_pos(self):
        '''
        Abre el TPV con el partner pre-cargado
        '''
        self.ensure_one()
        domain = [
            ('state', 'in', ['opening_control', 'opened']),
            ('user_id', '=', self.env.user.id),
            ('rescue', '=', False)
        ]
        pos_session = self.env['pos.session'].sudo().search(domain, limit=1)
        if not pos_session:
            domain = [
                ('state', 'in', ['opening_control', 'opened']),
                ('rescue', '=', False),
            ]
            pos_session = self.env['pos.session'].sudo().search(domain, limit=1)
        if not pos_session:
            raise UserError('No existe una sesion previamente abierta que se pueda usar. Debe abrir una sesion de TPV.')

        return {
            'type': 'ir.actions.act_url',
            'url': '/pos/ui?config_id=%s&partner_id=%s' % (pos_session.config_id.id, self.id),
            'target': 'new',
        }
