from odoo import api, fields, models


class OnpointTelegramGroup(models.Model):
    _inherit = 'onpoint.telegram.group'

    telegram_group_maintenance = fields.Boolean(string='Telegram Group Maintenance', default=False)

