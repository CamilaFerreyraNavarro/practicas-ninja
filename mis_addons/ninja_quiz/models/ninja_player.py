from odoo import models, fields, api

class NinjaPlayer(models.Model):
    _name = 'ninja.player'
    _description = 'Jugador del Quiz'

    name = fields.Char(string='Nombre del jugador', required=True)
    quiz_id = fields.Many2one('ninja.quiz', string='Quiz', required=True)
    total_score = fields.Integer(string='Puntaje total', compute='_compute_total_score', store=True)
    answer_ids = fields.One2many('ninja.player.answer', 'player_id', string='Respuestas')

    @api.depends('answer_ids.points_awarded')
    def _compute_total_score(self):
        for player in self:
            player.total_score = sum(player.answer_ids.mapped('points_awarded'))

class NinjaPlayerAnswer(models.Model):
    _name = 'ninja.player.answer'
    _description = 'Respuesta seleccionada por el jugador'

    player_id = fields.Many2one('ninja.player', string='Jugador', required=True, ondelete='cascade')
    question_id = fields.Many2one('ninja.question', string='Pregunta', required=True)
    answer_id = fields.Many2one('ninja.answer', string='Respuesta seleccionada', required=True)

    is_correct = fields.Boolean(string='¿Correcta?', compute='_compute_is_correct', store=True)
    points_awarded = fields.Integer(string='Puntos obtenidos', compute='_compute_points', store=True)

    @api.depends('answer_id.is_correct')
    def _compute_is_correct(self):
        for rec in self:
            rec.is_correct = rec.answer_id.is_correct

    @api.depends('answer_id.points', 'is_correct')
    def _compute_points(self):
        for rec in self:
            rec.points_awarded = rec.answer_id.points if rec.is_correct else 0
