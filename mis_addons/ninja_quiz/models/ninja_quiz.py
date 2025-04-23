from odoo import models, fields


class NinjaQuiz(models.Model):
    _name = 'ninja.quiz'
    _description = 'Cuestionario estilo kahoot'

    name = fields.Char('Nombre del Quiz', required=True)
    description = fields.Text('Descripción del Quiz')
    question_ids = fields.One2many('ninja.question', 'quiz_id', string='Preguntas')

class NinjaQuestion(models.Model):
    _name = 'ninja.question'
    _description = 'Pregunta del Quiz'

    name = fields.Char('Pregunta', required=True)
    image = fields.Binary(string='Imagen')
    quiz_id = fields.Many2one('ninja.quiz', string='Quiz')
    answer_ids = fields.One2many('ninja.answer', 'question_id', string='Respuestas')

class NinjaAnswer(models.Model):
    _name = 'ninja.answer'
    _description = 'Respuesta de la pregunta'

    name = fields.Char('Respuesta', required=True)
    question_id = fields.Many2one('ninja.question', string='Pregunta')
    is_correct = fields.Boolean('¡Es correcta!', default=False)
    points = fields.Integer(string="Puntos", default=0)

