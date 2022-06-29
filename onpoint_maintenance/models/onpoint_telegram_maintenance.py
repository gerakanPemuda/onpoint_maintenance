from odoo import api, fields, models
from datetime import datetime


class OnpointTelegramSupport(models.Model):
    _inherit = 'onpoint.telegram.group'

    support_id = fields.Many2one('onpoint.support', string='Support Name')
    telegram_group_maintenance = fields.Boolean(default=False)