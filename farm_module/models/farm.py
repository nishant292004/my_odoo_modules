from odoo import models,fields,api

class MyFarm(models.Model):
    
    _name = 'farm.model'
    _description = 'Farm Model'
    _rec_name = 'code'
    _parent_name = 'parent_id'
    _parent_store = True
    _order = 'farmer_id asc'
    
    farmer_id = fields.Many2one('farm.farmer',string="Farmer's Name")

    farm_size = fields.Float("Area Of Farm (Hectares)", digits=(10,3) , aggregator='avg')

    is_organic = fields.Boolean('Is Organic ?')

    description = fields.Text('Description')

    est_date = fields.Date('Establishment Date' , index=True, default = fields.Date.context_today)

    last_inspection = fields.Datetime('Last Inspection Date')

    farm_type = fields.Selection([('small','Small'),('medium','Medium'),('large','Large')],string='Farm Type')

    code = fields.Char(string='Farm Code', size=4)

    active = fields.Boolean(string='Active' , default = True, invisible=True)

    password = fields.Char('Password')

    is_hierarchy = fields.Boolean(string="Is In Hierarchy",default=False)

    email = fields.Char('Email')

    priority = fields.Selection([(str(ele),str(ele)) for ele in range(0,5)], 'Priority')

    harv_type = fields.Selection([
    ('organic', 'Organic Farm'),
    ('fruit', 'Fruit Farm'),
    ('vegetable', 'Vegetable Farm'),
    ('grain', 'Grain Farm')
    ], string='Harvest Type')

    crop_ids = fields.One2many(comodel_name='farm.crop',inverse_name='farm_id',string='Crop',ondelete='cascade')
    
    govt_total = fields.Float(compute='_calc_govt_price', string='Total Government Price (For All the Crops)', store=True)
    
    mrkt_total = fields.Float(compute='_calc_mrkt_price', string='Total Market Price (For All the Crops)', store=True)

    state = fields.Selection([('planting','Planting'),
                              ('maintenance','Maintenance'),
                              ('harvesting','Harvesting'),
                              ('stored','Stored'),
                              ('selling','Selling'),
                              ], default='planting')
                              
    sequence = fields.Integer('Sequence')

    parent_id = fields.Many2one('farm.model','Parent Farm',index=True, domain=[('is_organic','=','true')])

    child_ids = fields.One2many('farm.model','parent_id','Child Farms')

    parent_path = fields.Char('Parent Path',index=True)

    machine_ids = fields.Many2many('farm.machines',string='Machines',domain=[('name','ilike','c')])

    @api.depends('crop_ids')

    def _calc_govt_price(self):

        """
        This method is used to calculate the total govt price based on cost and govt profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.govt_total = sum(price.crop_ids.mapped('govt_price'))

    @api.depends('crop_ids')

    def _calc_mrkt_price(self):
        """
        This method is used to calculate the total market price based on cost and market profit margin.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """

        for price in self:
            price.mrkt_total = sum(price.crop_ids.mapped('mrkt_price'))


    # what is self ?
    # self is a recordset of the current model.which contains the model name and ids of the records.   

    def fetch_rec_set(self):
        """
        This method is used to fetch the blank record set of another model.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop']
        print(crop_obj)

    def fetch_one_rec_set(self):
        """
        This method is used to fetch the one record from record set.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        for farm in self:
            print(farm) 

    def fetch_val_rec_set(self):
        """
        This method is used to fetch the value of the record from the record set.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        for farm in self:
            print(farm.code) 
    
    def fetch_val_diff_rec_set(self):
        """
        This method is used to fetch the value of the record from the related model record set.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([])

        for crop in crop_obj:
            print(crop.name)
    
    def fetch_mul_diff_rec_set(self):
        """
        This method is used to fetch the value of the record from the related model with muliple recordset record set.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([])

        crop_names = crop_obj.mapped('name')
        print(crop_names)

    def fetch_one_ens_one(self):
        """
        This method is used to fetch the value of record set using ensure_one.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([('id','=',4)])
        crop_obj.ensure_one()

        crop_names = crop_obj.mapped('name')
        print(crop_names)  

    def fetch_mul_ens_one(self):
        """
        This method is used to fetch the value of record set using ensure_one.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([])
        crop_obj.ensure_one()

        crop_names = crop_obj.mapped('name')
        print(crop_names)        

    def fetch_meta_data_one(self):
        """
        This method is used to fetch the metadata of one record.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([('id','=',4)])
        print(crop_obj.get_metadata())  

    def fetch_meta_data_mul(self):
        """
        This method is used to fetch the metadata of multiple record.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop'].search([])
        print(crop_obj.get_metadata())  
