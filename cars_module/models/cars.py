from odoo import models,fields

class CarsDetails(models.Model):
    _name = 'cars.management'
    _description = 'Cars Management'
    _rec_name = 'car_name'

    car_name = fields.Char('Car Name')
    company_name = fields.Char('Company Name')

    color = fields.Integer('Color')
    manufacturing_date = fields.Date('Manufacture Date')

    engine_id = fields.Many2one('cars.engine','Engine')
    tagz_ids  = fields.Many2many(comodel_name='cars.tagz',relation='tagz_cars_rel', string='Tagz')   

    # TODO : paisa chuta karavana
    