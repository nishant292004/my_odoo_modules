from odoo import models,fields

class Farmer(models.Model):
    _name='farm.farmer'
    _description = 'farmer of the farm'

    name = fields.Char("Farmer's Name")
    age = fields.Integer(string="Age",aggregator='max')
    mo_no = fields.Char("Mobile no.")
    farm_id = fields.Many2one(comodel_name='farm.model', string='Farm Code', ondelete="restrict")
    crop_ids = fields.Many2many(comodel_name='farm.crop',string="Types Of Crops")
    machine_ids = fields.Many2many(comodel_name='farm.machines',relation='machine_farmer_rel',column1='machines_id',column2='farmer_id',string="Machines used in farm")