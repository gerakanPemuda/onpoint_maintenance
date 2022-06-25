from odoo import api, fields, models


class OnpointClient(models.Model):
    _name = 'onpoint.client'
    _description = 'Onpoint Support'

    name = fields.Text(string='Name', required=True, tracking=True)
    url = fields.Char(string='URL')
    support_ids = fields.One2many('onpoint.support', 'client_id')
