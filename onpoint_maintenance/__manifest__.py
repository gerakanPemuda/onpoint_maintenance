{
    'name': 'Onpoint Maintenance',
    'version': '1.0',
    'summary': 'Onpoint Maintenance Software',
    'sequence': -100,
    'description': """Onpoint Maintenance Software""",
    'category': 'Productivity',
    'website': 'https:',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'onpoint_telegram',  # nameModule
    ],
    'data': [
        'data/onpoint_support_sequence.xml',
        'views/onpoint_client_view.xml',
        'views/onpoint_support_view.xml',
        'views/onpoint_maintenance_menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
