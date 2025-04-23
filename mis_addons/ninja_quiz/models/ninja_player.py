from odoo import models, fields, api

class NinjaPlayer(models.Model):
    _name = 'ninja.player'
    _description = 'Jugador del Quiz'

    name = fields.Char(string='Nombre del jugador', required=True)
    quiz_id = fields.Many2one('ninja.quiz', string='Quiz', required=True)
    total_score = fields.Integer(string='Puntaje total', default=0)
    answer_ids = fields.One2many('ninja.player.answer', 'player_id', string='Respuestas')

class NinjaPlayerAnswer(models.Model):
    _name = 'ninja.player.answer'
    _description = 'Respuesta seleccionada por el jugador'

    player_id = fields.Many2one('ninja.player', string='Jugador', required=True)
    question_id = fields.Many2one('ninja.question', string='Pregunta', required=True)
    answer_id = fields.Many2one('ninja.answer', string='Respuesta seleccionada', required=True)

    is_correct = fields.Boolean(string='¿Correcta?', compute='_compute_is_correct', store=True)
    points_awarded = fields.Integer(string='Puntos obtenidos', compute='_compute_points', store=True)

    @api.depends('answer_id')
    def _compute_is_correct(self):
        for record in self:
            record.is_correct = record.answer_id.is_correct

    @api.depends('answer_id')
    def _compute_points(self):
        for record in self:
            record.points_awarded = record.answer_id.points if record.answer_id.is_correct else 0
