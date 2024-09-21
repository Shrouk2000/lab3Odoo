from odoo import models, fields, api, _

class HmsPatient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    department_id = fields.Many2one('hms.department', string='Department', required=True)
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors', readonly=True)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')

    log_history_ids = fields.One2many('hms.patient.log', 'patient_id', string='Log History')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = (fields.Date.today() - record.birth_date).days // 365
            else:
                record.age = 0

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.pcr = True
            return {'warning': {'title': _('Warning'), 'message': _('PCR has been checked automatically.')}}
        if self.age < 50:
            self.history = False

    @api.onchange('department_id')
    def _onchange_department(self):
        if self.department_id and not self.department_id.is_opened:
            return {'warning': {'title': _('Warning'), 'message': _('You cannot choose a closed department.')}}
        self.doctor_ids = [(5, 0, 0)]

    @api.model
    def create(self, vals):
        patient = super(HmsPatient, self).create(vals)
        patient.log_history_ids.create({
            'patient_id': patient.id,
            'description': _('Patient created.'),
            'created_by': self.env.user.id,
        })
        return patient
