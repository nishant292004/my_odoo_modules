from odoo import models,fields

class CarsPurchase(models.Model):
    _name = 'cars.purchase'
    _description = 'Information about purchase'
    _rec_name = 'cars_id'

    cars_id = fields.Many2one('cars.management','Car Name')
    car_price = fields.Integer(related='cars_id.price',string='Car Price')

    client_id = fields.Many2one('cars.client','Client')
    ph_no = fields.Char(related='client_id.ph_no',string='Phone No.')

