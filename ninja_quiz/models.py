from odoo import models, fields 

 class NinjaQuiz(models.Model):
	
	_name='ninja.quiz'
	_description='Ninja Quiz'

	name = fields.Char('Nombre del Quiz', requred=True)
	description = fields.Text('Descripción del Quiz')
	question_ids = fields.One2many('ninja.question', 'quiz_id', string='Questions')

 class NinjaQuestion(models.Model):

        _name='ninja.question'
        _description='Pregunta del Quiz'

        name = fields.Char('Pregunta', requred=True)
        quiz_id = fields.Many2one('ninja.quiz', string='Quiz')
        answer_ids = fields.One2many('ninja.answer', 'question_id', string='Respuestas')

 class NinjaAnswer(models.Model):

        _name='ninja.answer'
        _description='Respuesta de la pregunta'

        name = fields.Char('Respuesta', requred=True)
        question_id = fields.Many2one('ninja.question', string='Pregunta')
        is_correct = fields.Boolean('¡Es correcta!', default=False )
