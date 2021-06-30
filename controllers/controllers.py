# -*- coding: utf-8 -*-
# from odoo import http


# class BasicoGenerado9(http.Controller):
#     @http.route('/basico_generado9/basico_generado9/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basico_generado9/basico_generado9/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('basico_generado9.listing', {
#             'root': '/basico_generado9/basico_generado9',
#             'objects': http.request.env['basico_generado9.basico_generado9'].search([]),
#         })

#     @http.route('/basico_generado9/basico_generado9/objects/<model("basico_generado9.basico_generado9"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basico_generado9.object', {
#             'object': obj
#         })
