# -*- coding: utf-8 -*-
from odoo import api, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('company_id')
    def _check_company_id(self):
        super(CrmLead, self)._check_company_id()
        for rec in self:
            if not rec.company_id:
                continue
            order = self.env['sale.order'].search(
                [('opportunity_id', '=', rec.id),
                 ('company_id', '!=', rec.company_id.id)], limit=1)
            if order:
                raise ValidationError(
                    _('You cannot change the company, as this '
                      'Lead is assigned to Sales Order '
                      '%s.' % order.name))
