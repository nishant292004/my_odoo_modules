from odoo import models,fields

class Farmer(models.Model):
    _name='farm.farmer'
    _description = 'farmer of the farm'

    name = fields.Char("Farmer's Name")
    age = fields.Integer("Age")
    mo_no = fields.Char("Mobile no.")
    crop_ids = fields.Many2many(comodel_name='farm.crop',string="Specialization (Crops)")