from odoo import models,fields

class CarsDetails(models.Model):
    _name = 'cars.management'
    _description = 'Cars Management'
    _rec_name = 'car_name'

    car_name = fields.Char('Car Name')
    company_name = fields.Char('Company Name')

    # engine_id = fields.Many2one(comodel_name='school.standard', string='Engine')
    color = fields.Integer('Color')
    manufacturing_date = fields.Date('Manufacture Date')

    engine_id = fields.Many2one('cars.engine','Engine')