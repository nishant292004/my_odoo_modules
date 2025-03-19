from odoo import models,fields

class CarsClient(models.Model):
    _name = 'cars.client'
    _description = 'Information about client'
    _rec_name = 'name'

    name = fields.Char('Name', required=True)
    ph_no = fields.Char('Phone No.', required=True)
