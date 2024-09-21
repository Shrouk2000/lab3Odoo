from odoo import models, fields

class HmsPatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patient Log History'

    patient_id = fields.Many2one('hms.patient', string='Patient', required=True)
    description = fields.Text(string='Description')
    created_by = fields.Many2one('res.users', string='Created By', readonly=True)
    date = fields.Datetime(default=fields.Datetime.now)
