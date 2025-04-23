
{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'summary': 'Clon de Kahoot con Odoo',
    'depends': ['website', 'base', 'survey'],
    'data': [
	'security/ir.model.access.csv',
        'views/ninja_quiz_views.xml',
	'views/ninja_quiz_templates.xml',
    ],


    'installable': True,
    'application': True,
}
