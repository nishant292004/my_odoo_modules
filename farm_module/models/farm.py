from odoo import models,fields

class MyFarm(models.Model):
    _name = 'farm.model'
    _description = 'Farm Model'
    _rec_name = 'farmer_name'
    _order = 'farmer_name asc'

    farmer_name = fields.Char("Farmer's Name", required=True)
    farm_size = fields.Float("Area Of Farm (Hectares)",required=True, digits=(10,3))
    is_organic = fields.Boolean('Is Organic ?')
    description = fields.Text('Description')
    est_date = fields.Date('Establishment Date',required=True , index=True, default = fields.Date.context_today)
    last_inspection = fields.Datetime('Last Inspection Date',required=True)
    farm_type = fields.Selection([('small','Small'),('medium','Medium'),('large','Large')],string='Farm Type',required=True)
    code = fields.Char(string='Farm Code', size=4)
    active = fields.Boolean(string='Active' , default = True, invisible=True)
    password = fields.Char('Password')
    email = fields.Char('Email')
    priority = fields.Selection([(str(ele),str(ele)) for ele in range(0,5)], 'Priority')
    harv_type = fields.Selection([
    ('organic', 'Organic Farm'),
    ('fruit', 'Fruit Farm'),
    ('vegetable', 'Vegetable Farm'),
    ('grain', 'Grain Farm')
    ], string='Harvest Type', required=True)
    crop_id = fields.Many2one(comodel_name='farm.crop',string='Crop')
    code_cr = fields.Char(related='crop_id.code',string='Code')

