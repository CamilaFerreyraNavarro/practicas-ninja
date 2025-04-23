from odoo import http
from odoo.http import request

class NinjaQuizController(http.Controller):

    @http.route('/jugar', auth='public', website=True)
    def jugar_inicio(self, **kw):
        quizzes = request.env['ninja.quiz'].sudo().search([])
        return request.render('ninja_quiz.jugar_inicio', {'quizzes': quizzes})

    @http.route('/jugar/quiz', auth='public', website=True)
    def jugar_quiz(self, quiz_id=0, step=0, respuesta_id=None, player_id=0, **kw):
        quiz = request.env['ninja.quiz'].sudo().browse(int(quiz_id))
        preguntas = quiz.question_ids.sorted('id')
        step = int(step)
        player_id = int(player_id)

        if respuesta_id:
            respuesta_id = int(respuesta_id)
            respuesta = request.env['ninja.answer'].sudo().browse(respuesta_id)

            pregunta = respuesta.question_id

            request.env['ninja.player.answer'].sudo().create({
                'player_id': player_id,
                'question_id': pregunta.id,
                'answer_id': respuesta.id,
            })

        if step >= len(preguntas):
            jugador = request.env['ninja.player'].sudo().browse(player_id)
            return request.render('ninja_quiz.jugar_resultado', {
                'jugador': jugador,
            })

       pregunta = preguntas[step]
        return request.render('ninja_quiz.jugar_pregunta', {
            'quiz': quiz,
            'pregunta': pregunta,
            'step': step,
            'next_step': step + 1,
            'player_id': player_id,
        })

    @http.route('/jugar/quiz', auth='public', website=True)
    def jugar_quiz(self, quiz_id=0, step=0, **kw):
        quiz = request.env['ninja.quiz'].sudo().browse(int(quiz_id))
        preguntas = quiz.question_ids.sorted('id')  
        step = int(step)

        if step >= len(preguntas):
            return request.render('ninja_quiz.jugar_resultado', {
                'quiz': quiz,
            })

        pregunta = preguntas[step]
        return request.render('ninja_quiz.jugar_pregunta', {
            'quiz': quiz,
            'pregunta': pregunta,
            'step': step,
            'next_step': step + 1,
        })

    @http.route('/jugar/empezar', type='http', auth='public', website=True, methods=['POST'])
    def jugar_empezar(self, **post):
        nombre = post.get('nombre')
        quiz_id = int(post.get('quiz_id'))

        player = request.env['ninja.player'].sudo().create({
            'name': nombre,
            'quiz_id': quiz_id,
        })

        return request.redirect(f'/jugar/quiz?quiz_id={quiz_id}&step=0&player_id={player.id}')
