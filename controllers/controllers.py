# -*- coding: utf-8 -*-
from odoo import http

# class VitEoffice(http.Controller):
#     @http.route('/vit_eoffice/vit_eoffice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_eoffice/vit_eoffice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_eoffice.listing', {
#             'root': '/vit_eoffice/vit_eoffice',
#             'objects': http.request.env['vit_eoffice.vit_eoffice'].search([]),
#         })

#     @http.route('/vit_eoffice/vit_eoffice/objects/<model("vit_eoffice.vit_eoffice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_eoffice.object', {
#             'object': obj
#         })