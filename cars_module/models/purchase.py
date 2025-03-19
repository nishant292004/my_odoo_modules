from odoo import models,fields,api

class CarsPurchase(models.Model):
    _name = 'cars.purchase'
    _description = 'Information about purchase'
    _rec_name = 'cars_id'

    cars_id = fields.Many2one('cars.management','Car Name', required=True)
    car_price = fields.Integer(related='cars_id.price',string='Car Price')

    client_id = fields.Many2one('cars.client','Client', required=True)
    ph_no = fields.Char(related='client_id.ph_no',string='Phone No.')

    car_bill = fields.Integer(compute='_calc_price' , string='Total Bill', store=True)
    brokerage = fields.Integer(compute='_calc_brokerage',string='Brokerage(10%)', store=True)

    @api.depends('car_price')

    def _calc_brokerage(self):
        """
        This method is used to calculate the total brokerage amount of the car price
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for car in self:
            car.brokerage = (car.car_price * 10)/100

    @api.depends('car_price','brokerage')

    def _calc_price(self):
        """
        This method is used to calculate the total brokerage amount of the car price
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for car in self:
            car.car_bill = car.car_price + car.brokerage

