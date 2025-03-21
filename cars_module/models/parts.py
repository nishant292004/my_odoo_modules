from odoo import models,fields

class CarsParts(models.Model):
    _name = 'cars.parts'
    _description = 'parts for cars'

    name = fields.Char('Name of part')
    price = fields.Integer('Price')
    