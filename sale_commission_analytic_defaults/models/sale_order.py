# -*- coding: utf-8 -*-

from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def _default_agents(self):
        project_id = self.env.context.get('project_id')
        if not project_id:
            return super(SaleOrderLine, self)._default_agents()

        project = self.env['account.analytic.account'].browse(project_id)

        agents = []
        for default_agent_commission in project.default_agents:
            agents.append({
                'agent': default_agent_commission.agent.id,
                'commission': default_agent_commission.commission.id,
            })

        return [(0, 0, agent) for agent in agents]

    agents = fields.One2many(
        string="Agents & commissions",
        comodel_name='sale.order.line.agent', inverse_name='sale_line',
        copy=True, readonly=True, default=_default_agents)
