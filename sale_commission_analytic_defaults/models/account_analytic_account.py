# -*- coding: utf-8 -*-

from openerp import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    def _check_agent_one_time(self, cr, uid, ids, context=None):
        for account in self.browse(cr, uid, ids):
            agent_ids = [x.agent.id for x in account.default_agents]
            duplicates = [x for x in agent_ids if agent_ids.count(x) > 1]
            if duplicates:
                return False

        return True

    @api.model
    def _prepare_invoice_line(self, line, fiscal_position):
        res = super(AccountAnalyticAccount, self)._prepare_invoice_line(
            line, fiscal_position)

        agents = []
        for default_agent_commission in line.analytic_account_id.default_agents:
            agents.append((0, 0, {
                'agent': default_agent_commission.agent.id,
                'commission': default_agent_commission.commission.id,
            }))

        res['agents'] = agents
        return res

    default_agents = fields.Many2many(
        comodel_name='analytic.account.agent.line',
        string='Default Agents and Commissions')

    _constraints = [
        (_check_agent_one_time,
         'You can only add one time each agent.',
         ['default_agents']),
    ]


class AnalyticAccountAgentLine(models.Model):
    _name = 'analytic.account.agent.line'

    agent = fields.Many2one(
        comodel_name='res.partner', required=True,
        domain="[('agent', '=', True')]")
    commission = fields.Many2one(
        comodel_name='sale.commission', required=True)
