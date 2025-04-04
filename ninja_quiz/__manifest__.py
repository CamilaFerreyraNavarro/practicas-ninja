{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Clon de Kahoot para Odoo',
    'depends': ['survey'],
    'data': [
        'views/ninja_quiz_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
