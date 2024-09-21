from odoo import models, fields

class HmsDoctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    image = fields.Binary()