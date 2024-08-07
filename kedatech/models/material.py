from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'kedatech.material'

    code = fields.Integer(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    buy_price = fields.Float('Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier Name', required=True)

    @api.model
    def create(self, vals):
        if 'buy_price' in vals:
            vals['buy_price'] = int(vals['buy_price'])
            if vals['buy_price'] < 100:
                raise ValidationError('The Material Buy Price must be greater than 100.')
        return super(Material, self).create(vals)

    def write(self, vals):
        if 'buy_price' in vals:
            vals['buy_price'] = int(vals['buy_price'])
            if vals['buy_price'] < 100:
                raise ValidationError('The Material Buy Price must be greater than 100.')
        return super(Material, self).write(vals)

