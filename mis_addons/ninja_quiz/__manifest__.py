
{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'summary': 'Clon de Kahoot con Odoo',
    'depends': ['base', 'survey'],
    'data': [
	'security/ir.model.access.csv',
        'views/ninja_quiz_views.xml',
    ],


    'installable': True,
    'application': True,
}
