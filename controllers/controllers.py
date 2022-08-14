# -*- coding: utf-8 -*-
from odoo import http

# class Bikeshop(http.Controller):
#     @http.route('/bikeshop/bikeshop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bikeshop/bikeshop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bikeshop.listing', {
#             'root': '/bikeshop/bikeshop',
#             'objects': http.request.env['bikeshop.bikeshop'].search([]),
#         })

#     @http.route('/bikeshop/bikeshop/objects/<model("bikeshop.bikeshop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bikeshop.object', {
#             'object': obj
#         })