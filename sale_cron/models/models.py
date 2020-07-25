# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import datetime
from urllib import urlencode
from urlparse import urljoin


class sale_cron(models.Model):
    _inherit = 'crm.lead'

    day_earlier = fields.Integer(
        String='Nombre de jour',
        default=0
    )

    def _trigger_action(self, date_action, current_date, day_earlier):
        base_date_action = datetime.datetime.strptime(date_action, '%Y-%m-%d')
        reminder_date = (base_date_action - datetime.timedelta(days=day_earlier)).strftime("%Y-%m-%d")
        if date_action == current_date or current_date == reminder_date:
            return 0
        return -1

    def get_current_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        params = {
            'id': self.id,
            'db': self.env.cr.dbname,
            'model': 'crm.lead',
            'view_type': 'form',
            'menu_id': self.env.ref('crm.menu_crm_opportunities').id,
            'action': self.env.ref('crm.crm_lead_opportunities_tree_view').id
        }
        url = urljoin(base_url+'/web', "#%s" % urlencode(params))
        return url

    @api.multi
    def _check_crm_lead(self):
        template = self.env.ref('sale_cron.crm_lead_reminder')
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        for crm_lead_id in self.search([('stage_id', '!=', self.env.ref('crm.stage_lead4').id)]):
            i = self._trigger_action(crm_lead_id.date_action, current_date, crm_lead_id.day_earlier)
            if i == -1:
                continue
            template.send_mail(crm_lead_id.id, force_send=True, raise_exception=True)

        return 0
