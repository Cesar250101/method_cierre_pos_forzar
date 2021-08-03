# -*- coding: utf-8 -*-
from odoo import http

# class MethodCierrePosForzar(http.Controller):
#     @http.route('/method_cierre_pos_forzar/method_cierre_pos_forzar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_cierre_pos_forzar/method_cierre_pos_forzar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_cierre_pos_forzar.listing', {
#             'root': '/method_cierre_pos_forzar/method_cierre_pos_forzar',
#             'objects': http.request.env['method_cierre_pos_forzar.method_cierre_pos_forzar'].search([]),
#         })

#     @http.route('/method_cierre_pos_forzar/method_cierre_pos_forzar/objects/<model("method_cierre_pos_forzar.method_cierre_pos_forzar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_cierre_pos_forzar.object', {
#             'object': obj
#         })