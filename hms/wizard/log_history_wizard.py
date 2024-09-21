from odoo import models, fields, api, _

class LogHistoryWizard(models.TransientModel):
    _name = 'hms.patient.log.wizard'
    _description = 'Log History Wizard'

    patient_id = fields.Many2one('hms.patient', string='Patient', required=True)
    description = fields.Text(string='Description', required=True)

    def action_add_log(self):
        self.ensure_one()
        self.patient_id.log_history_ids.create({
            'patient_id': self.patient_id.id,
            'description': self.description,
            'created_by': self.env.user.id,
        })
