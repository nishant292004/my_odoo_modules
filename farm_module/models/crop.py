from odoo import models,fields

class FarmCrop(models.Model):
    _name = 'farm.crop'
    _description = 'farm crop'

    name = fields.Char('Crop Name')
    crop_type = fields.Selection([('monsoon','Monsoon Season'),('winter','Winter Season'),('short','Short Season')],string='Type Of Crop')
    code = fields.Char(string='Code',size=4)
    farm_ids = fields.One2many(comodel_name='farm.model',inverse_name='crop_id',string='Farm')
    cost = fields.Float('cost')
    govt_add = fields.Float("Government's Profit Margin (%)")
    mrkt = fields.Float("Market's Profit Margin (%) ")