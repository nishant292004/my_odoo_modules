from odoo import models,fields,api

class CarsService(models.Model):
    _name = 'cars.service'
    _description = 'the cars service model'
    _rec_name = 'car_name'

    car_name = fields.Many2one(comodel_name='cars.management',string='Car Name')
    parts_ids = fields.Many2many(comodel_name='cars.parts',string='Add Parts')
    price = fields.Integer(related='parts_ids.price')
    total_price = fields.Integer(compute='calc_price', string='Total Price')

    @api.depends('price')
    def calc_price(self):

        for record in self:
            record.total_price = sum(record.parts_ids.mapped('price'))
