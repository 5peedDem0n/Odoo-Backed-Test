from pickle import FALSE
from sqlite3 import Date
from requests import session
from datetime import datetime
from datetime import date

from odoo import http, _, exceptions
from odoo.http import request
from functools import partial
from attr import fields
import base64
import io
import json

class CRUDKedatech(http.Controller):
    @http.route('/kedatech/login', auth='public', methods=["POST"], csrf=False, cors="*", website=False)
    def login(self, **kw):
        # Validation
        try:
            login = kw["login"]
        except KeyError:
            raise exceptions.AccessDenied(message='`login` is required.')

        try:
            password = kw["password"]
        except KeyError:
            raise exceptions.AccessDenied(message='`password` is required.')

        try:
            db = kw["db"]
        except KeyError:
            raise exceptions.AccessDenied(message='`db` is required.')

        # Auth user
        http.request.session.authenticate(db, login, password)
        # Session info
        res = request.env['ir.http'].session_info()
        company_id = res.get('company_id')
        company = request.env['res.company'].search([
            ('id', '=', company_id)
        ])
        res['company_phone'] = company.phone
        return request.make_response(json.dumps(res), headers={'Content-Type': 'application/json'})

    @http.route('/kedatech/material/update/<int:record_id>', auth='public', methods=["POST"], csrf=False, cors="*", website=False)
    def updateMaterial(self, record_id, **kw):
        material = request.env['kedatech.material'].sudo().search([
            ("id", "=", record_id)
        ])

        material = material[0]
        if material:
            material.write({
                'name': kw['name'],
                'buy_price': kw['price'],
                })

        return request.make_response(json.dumps( {
            'status': 'success',
            'message': f'Material dengan id {material.id} Berhasil di Update',
        }), headers={'Content-Type': 'application/json'})

    @http.route('/kedatech/material/delete/<int:record_id>', auth='public', methods=["POST"], csrf=False, cors="*", website=False)
    def deleteMaterial(self, record_id, **kw):
        material = request.env['kedatech.material'].sudo().search([
            ("id", "=", record_id)
        ])

        material = material[0]
        if material:
            material.unlink()

        return request.make_response(json.dumps( {
            'status': 'success',
            'message': f'Material dengan id {material.id} Berhasil di Delete',
        }), headers={'Content-Type': 'application/json'})

    