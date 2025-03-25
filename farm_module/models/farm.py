from odoo import models,fields

class MyFarm(models.Model):
    _name = 'farm.model'
    _description = 'Farm Model'
    _rec_name = 'farmer_name'
    _order = 'farmer_name asc'

    farmer_name = fields.Char("Farmer's Name", required=True)
    farm_size = fields.Float("Area Of Farm (Hectares)",required=True)
    is_organic = fields.Boolean('Is Organic ?')
    description = fields.Text('Description')
    est_date = fields.Date('Establishment Date',required=True , index=True, default = fields.Date.context_today)
    last_inspection = fields.Datetime('Last Inspection Date',required=True)
    farm_type = fields.Selection([('small','Small'),('medium','Medium'),('large','Large')],string='Farm Type',required=True)
