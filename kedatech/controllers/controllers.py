# -*- coding: utf-8 -*-
from odoo import http

# class BookingOrder(http.Controller):
#     @http.route('/booking_order/booking_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order/booking_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order.listing', {
#             'root': '/booking_order/booking_order',
#             'objects': http.request.env['booking_order.booking_order'].search([]),
#         })

#     @http.route('/booking_order/booking_order/objects/<model("booking_order.booking_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order.object', {
#             'object': obj
#         })