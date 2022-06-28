from odoo import api, fields, models
from datetime import datetime


class OnpointSupport(models.Model):
    _name = 'onpoint.support'
    _description = 'Onpoint Support'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    support_type = fields.Selection([
        ('bug', 'Bug Fixing'),
        ('request', 'New Request'),
    ], default='bug', tracking=True)
    client_id = fields.Many2one('onpoint.client')
    notes = fields.Text(required=True)
    complete_notes = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
        ('in_process', 'In Process'),
        ('complete', 'Completed')
    ], default='draft')
    state_bug = fields.Selection(related='state')
    state_request = fields.Selection(related='state')
    state_approve = fields.Selection(related='state')
    state_reject = fields.Selection(related='state')

    submit_date = fields.Date(default=datetime.now())
    approve_reject_date = fields.Date(default=fields.Datetime.now, string='Approve/Reject Date')
    start_date = fields.Date(default=fields.Datetime.now)
    complete_date = fields.Date(default=fields.Datetime.now)

    def action_submit(self):
        self.state = 'submit'

    def action_approve(self):
        self.state = 'approve'

    def action_reject(self):
        self.state = 'reject'

    def action_in_process(self):
        self.state = 'in_process'

    def action_complete(self):
        self.state = 'complete'
