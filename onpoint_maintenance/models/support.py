from odoo import api, fields, models


class OnpointSupport(models.Model):
    _name = 'onpoint.support'
    _description = 'Onpoint Support'

    support_type = fields.Selection([
        ('bug', 'Bug Fixing'),
        ('request', 'New Request'),
    ], default='bug')
    client_id = fields.Many2one('onpoint.client')
    notes = fields.Text(required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('in_process', 'In Process'),
        ('complete', 'Complete')
    ], default='draft',)
    submit_date = fields.Date()
    approve_reject_date = fields.Date()
    start_date = fields.Date()
    complete_date = fields.Date()


