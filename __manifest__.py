{
    'name': 'Hospital Management',
    'version': '1.2',
    'author': 'Abdirahmaan',
    'category': 'Hospital',
    'sequence': -100,  # Adjust the sequence number as needed
    'summary': 'Hospital Management System',
    'description': """Hospital Management System.""",
    'depends': ['mail', 'product'],
    'exclude': [],  # Corrected field name
    'data': [
        'secuirty/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patien_tag_view.xml',
        'views/odoo_playground_view.xml',
        'wizard/cancel_appointment_view.xml',

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
