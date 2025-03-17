from odoo import models,fields

class CarsEngine(models.Model):
    _name = 'cars.engine'
    _description = 'This is field for cars engine'

    name = fields.Char('Type Of Engine')