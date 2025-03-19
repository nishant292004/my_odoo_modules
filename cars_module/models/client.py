from odoo import models,fields

class CarsClient(models.Model):
    _name = 'cars.client'
    _description = 'Information about client'
    _rec_name = 'name'

    name = fields.Char('Name')
    ph_no = fields.Char('Phone No.')
