from odoo import models,fields,api

class FarmCrop(models.Model):
    _name = 'farm.crop'
    _description = 'farm crop'

    name = fields.Char('Crop Name')
    crop_type = fields.Selection([('monsoon','Monsoon Season'),('winter','Winter Season'),('short','Short Season')],string='Type Of Crop')
    code = fields.Char(string='Code',size=4)
    farm_ids = fields.Many2one(comodel_name='farm.model',string='Farm Code')
    cost = fields.Float('Cost (Rs.)')
    govt_add = fields.Float("Government's Profit Margin (%)")
    mrkt = fields.Float("Market's Profit Margin (%) ")

    govt_price = fields.Float(compute='_calc_govt_price', string='Government Price (Rs.)')
    mrkt_price = fields.Float(compute='_calc_mrkt_price', string='Market Price (Rs.)')

    @api.depends('cost','govt_add')

    def _calc_govt_price(self):

        """
        This method is used to calculate the total govt price based on cost and govt profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.govt_price = price.cost + (price.cost * price.govt_add)/100

    @api.depends('cost','mrkt')

    def _calc_mrkt_price(self):
        """
        This method is used to calculate the total market price based on cost and market profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.mrkt_price = price.cost + (price.cost * price.mrkt)/100
              
