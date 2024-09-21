{
    'name': 'HMS',
    'version': '17.0.0.1.0',
    'summary': 'Manage patients, departments, and doctors',
    'description': 'This module handles patient, department, and doctor management.',
    'category': 'Healthcare',
    'author': 'shrouk',
    'depends': ['base'],
    'data': [
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'wizard/log_history_wizard.xml',
    ],
}
