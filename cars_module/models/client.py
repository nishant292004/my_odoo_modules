from odoo import models,fields

class CarsClient(models.Model):
    _name = 'cars.client'
    _description = 'Information about client'
    _rec_name = 'name'

    cars_ids = fields.Many2one(comodel_name='cars.management',string='Cars')
    name = fields.Char('Name', required=True)
    ph_no = fields.Char('Phone No.', required=True)