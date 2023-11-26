# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _, tools
from odoo.exceptions import ValidationError
from odoo.tools import float_is_zero, float_compare



class Picking(models.Model):

    _inherit = "stock.picking"

    is_sent = fields.Boolean(string='Already sent by mail', default=False)

    def action_picking_send(self):
        self.ensure_one()
        template_id = self.env['ir.model.data']._xmlid_to_res_id('stock_picking_send_bymail.email_template_stock_picking', raise_if_not_found=False)
        lang = self.env.context.get('lang')
        template = self.env['mail.template'].browse(template_id)
        if template.lang:
            lang = template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': self._name,
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'force_email': True,
            'model_description': _('Delivery'),
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        self.write({'is_sent': True})
        return super(Picking, self).message_post(**kwargs)