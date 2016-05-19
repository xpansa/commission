# -*- coding: utf-8 -*-

from openerp import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def onchange_account_analytic_id(self, cr, uid, ids, account_analytic_id):
        if not account_analytic_id:
            return {'value': {'agents': []}}

        account_analytic_model = self.pool.get('account.analytic.account')
        account_analytic = account_analytic_model.browse(cr, uid, account_analytic_id)

        agents = []
        for default_agent_commission in account_analytic.default_agents:
            agents.append({
                'agent': default_agent_commission.agent.id,
                'commission': default_agent_commission.commission.id,
            })

        return {'value': {'agents': [(0, 0, agent) for agent in agents]}}
