from odoo import models,fields

class CarsDetails(models.Model):
    _name = 'cars.management'
    _description = 'Cars Management'
    _rec_name = 'car_name'

    car_name = fields.Char('Car Name', required=True)
    company_name = fields.Char('Company Name', required=True)

    price = fields.Integer('Car price', required=True)

    color = fields.Integer('Color')
    manufacturing_date = fields.Date('Manufacture Date')

    engine_id = fields.Many2one('cars.engine','Engine')
    tagz_ids  = fields.Many2many(comodel_name='cars.tagz',relation='tagz_cars_rel', string='Tagz')   

    client_ids = fields.One2many(comodel_name='cars.client',inverse_name ='cars_ids',string='Client')
    # ph_no = fields.Char(related='client_id.ph_no',string='Phone No.')

    