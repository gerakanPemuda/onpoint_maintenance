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
    ],
    'data': [
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
