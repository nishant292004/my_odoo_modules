from odoo import models,fields,api

class MyFarm(models.Model):
    
    _name = 'farm.model'
    _description = 'Farm Model'
    _rec_name = 'code'
    _order = 'farmer_name asc'

    farmer_name = fields.Char("Farmer's Name", required=True)

    farm_size = fields.Float("Area Of Farm (Hectares)",required=True, digits=(10,3) , aggregator='avg')

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

    crop_id = fields.One2many(comodel_name='farm.crop',inverse_name='farm_ids',string='Crop',ondelete='cascade')
    
    govt_total = fields.Float(compute='_calc_govt_price', string='Total Government Price (For All the Crops)')
    mrkt_total = fields.Float(compute='_calc_mrkt_price', string='Total Market Price (For All the Crops)')

    state = fields.Selection([('planting','Planting'),
                              ('maintenance','Maintenance'),
                              ('harvesting','Harvesting'),
                              ('stored','Stored'),
                              ('selling','Selling'),
                              ], default='planting')
    sequence = fields.Integer('Sequence')

    parent_id = fields.Many2one('farm.model','Parent Farm')

    child_ids = fields.One2many('farm.model','parent_id','Child Farms')

    parent_path = fields.Char('Parent Path', index=True)





    @api.depends('crop_id')

    def _calc_govt_price(self):

        """
        This method is used to calculate the total govt price based on cost and govt profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.govt_total = sum(price.crop_id.mapped('govt_price'))

    @api.depends('crop_id')

    def _calc_mrkt_price(self):
        """
        This method is used to calculate the total market price based on cost and market profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.mrkt_total = sum(price.crop_id.mapped('mrkt_price'))

