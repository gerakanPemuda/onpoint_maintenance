from odoo import api, fields, models, _
from datetime import datetime, timedelta


class OnpointSupport(models.Model):
    _name = 'onpoint.support'
    _description = 'Onpoint Support'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'api.telegram.abstract']

    name = fields.Char(string='Maintenance', required=True, copy=False, readonly=True, default=_('New'))
    support_type = fields.Selection([
        ('bug', 'Bug Fixing'),
        ('request', 'New Request'),
    ], default='bug', tracking=True)
    client_id = fields.Many2one('onpoint.client', required=True)
    notes = fields.Text(required=True)
    complete_notes = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
        ('in_process', 'In Process'),
        ('complete', 'Completed')
    ], tracking=True, default='draft', string='Status')
    state_bug = fields.Selection(related='state', tracking=False)
    state_request = fields.Selection(related='state', tracking=False)
    state_approve = fields.Selection(related='state', tracking=False)
    state_reject = fields.Selection(related='state', tracking=False)

    submit_date = fields.Date(default=datetime.now())
    approve_reject_date = fields.Date()
    start_date = fields.Date()
    complete_date = fields.Date()

    telegram_group_maintenance_ids = fields.Many2one('onpoint.telegram.group')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('onpoint.support') or _('New')
        res = super(OnpointSupport, self).create(vals)
        return res

    def action_submit(self):
        self.state = 'submit'
        message = dict(self._fields['support_type'].selection).get(self.support_type) + "\n"
        message += (self.submit_date + timedelta(hours=7)).strftime('%d %B %y') + "\n"
        message += "\n"
        message += self.client_id.name + "\n"
        message += "\n"
        message += "Notes:" + "\n"
        message += self.notes + "\n\n"
        message += "(by: " + self.env.user.name + ")" + "\n"
        message += "\n"
        message += "&#35;" + self.name

        params = {
            'chat_id': '413579342',
            'message': message
        }
        result = self.send_message(params)

    def action_approve(self):
        self.state = 'approve'
        self.approve_reject_date = datetime.today()

    def action_reject(self):
        self.state = 'reject'
        self.approve_reject_date = datetime.today()

    def action_in_process(self):
        self.state = 'in_process'
        self.start_date = datetime.today()

    def action_complete(self):
        self.state = 'complete'
        self.complete_date = datetime.today()


