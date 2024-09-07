{
    'name': 'Leaves Approval',
    'version': '1.0',
    'summary': 'Custom module to extend leaves functionality',
    'description': 'This module extends the leaves functionality in Odoo.',
    'category': 'Human Resources',
    'author': 'Khalid Al Salti',
    'website': 'https://atawah.com',
    'depends': ['hr', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}