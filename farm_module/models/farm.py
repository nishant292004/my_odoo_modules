from odoo import models,fields,api,Command

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

    def filt_data(self):
        """
        This method is used to filter the record.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        farm_data = self.env['farm.model'].search([])
        fill_rec = farm_data.filtered('farmer_id')
        print(fill_rec)

    def filt_data_lambda(self):
        """
        This method is used to filter the record using lambda.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        farm_data = self.env['farm.model'].search([])
        fill_rec = farm_data.filtered(lambda rec:rec.farmer_id)
        print(fill_rec)

    def filt_data_opp(self):
        """
        This method is used to filter the opposite record using lambda.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        farm_data = self.env['farm.model'].search([])
        fill_rec = farm_data.filtered(lambda rec: not rec.farmer_id)
        print(fill_rec)         

    def filt_mult_cond(self):
        """
        This method is used to filter the record using multple conditions.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        farm_data = self.env['farm.model'].search([])
        fill_rec = farm_data.filtered(lambda rec: not rec.farmer_id and rec.farm_type)
        print(fill_rec) 

    def mult_rec_in_list(self):
        """
        This method is used to filter the record using a single list.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        all_rec = [(rec.code,rec.farm_type,rec.farmer_id.name) for rec in self] 
        print(all_rec)
    
    
    def cond_in_list(self):
        """
        This method is used to filter the record using condition in a single list.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        concat_list = [rec.code+'-'+rec.farm_type for rec in self] 
        print(concat_list) 

    def sorted_rec(self):
        """
        This method is used to sort the records using condition.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        obj = self.env['farm.model'].search([])
        sort_recs = obj.sorted('farm_size')   
        print(sort_recs)     

    def sorted_rec_lambda(self):
        """
        This method is used to sort the records using lambda condition.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        obj = self.env['farm.model'].search([])
        sort_recs = obj.sorted(lambda rec:rec.farm_size)   
        print(sort_recs)    

    def sorted_rec_lambda_rev(self):
        """
        This method is used to sort the records in descending order using lambda condition.
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        obj = self.env['farm.model'].search([])
        sort_recs = obj.sorted(lambda rec:rec.farm_size,reverse=True)   
        print(sort_recs)      

    def create_rec_O2M(self):
        
        """
        This method is used to create O2M records .
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {'code':'DUMY',
            'crop_ids':[(0,0,{
                'name':'millets',
                'crop_type':'monsoon',
                'farm_id' : self.id,
                'code':'MILT',
                'cost':'7230.0',
                'govt_add':'56.0',
                'mrkt': '78.0'
            }   ),
            (Command.create({
                'name':'grains',
                'crop_type':'winter',
                'farm_id' : self.id,
                'code':'GRAN',
                'cost':'8600.0',
                'govt_add':'56.0',
                'mrkt': '78.0'
            })   )],
            
        } 
        new_crop = self.create(new_rec)
        print("O2M field created",new_crop)

    def create_rec_M2M(self):
        
        """
        This method is used to create M 2M records .
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {'code':'DUMY',
            'machine_ids':[
                (4,2),
                (4,5),
                (Command.link(6))],
            
        } 
        new_crop = self.create(new_rec)
        print("M2M field created",new_crop)

    def create_rec_set_M2M(self):
        
        """
        This method is used to create M2M records and remove existing one .
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {'code':'DUMY',
            'machine_ids':[
                (6,0,[1,4]),
                (Command.set([7]))],
            
        } 
        new_crop = self.create(new_rec)
        print("M2M field created",new_crop)  
        
    def write_rec_O2M(self):
        
        """
        This method is used to write O2M records .
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {'code':'DUMY',
            'crop_ids':[(0,0,{
                'name':'millets',
                'crop_type':'monsoon',
                'farm_id' : self.id,
                'code':'MILT',
                'cost':'7230.0',
                'govt_add':'56.0',
                'mrkt': '78.0'
            }   ),
            (Command.create({
                'name':'grains',
                'crop_type':'winter',
                'farm_id' : self.id,
                'code':'GRAN',
                'cost':'8600.0',
                'govt_add':'56.0',
                'mrkt': '78.0'
            })   )],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M field created",new_crop)

    def update_o2m_rec(self):
        
        """
        This method is used to update existing O2M records .
        ----------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (1,64,{'name':'chana'}),
                (Command.update(65,{'name':'bhinda'}))],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  
  
    def delete_o2m_rec(self):
        
        """
        This method is used to delete existing O2M records .
        ----------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (2,62),
                (Command.delete(63))],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  

    def unlink_o2m_rec(self):
        
        """
        This method is used to delete existing O2M records but not from database .
        -------------------------------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (3,1),
                (Command.unlink(2))],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  

    def link_o2m_rec(self):
        
        """
        This method is used to add existing O2M records.
        ------------------------------------------------
        @param self: object pointer
        """
        
        for rec in self:  
          
            new_rec =  {
            'crop_ids':[
                (4,1),
                (Command.link(2))],
            
            } 
            new_crop = rec.write(new_rec)
            print("O2M UPDATED",new_crop)  

    def clear_o2m_rec(self):
        
        """
        This method is used to clear existing O2M records.
        ------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (5,),
                (Command.clear())],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  

    def change_o2m_rec(self):
        
        """
        This method is used to change existing O2M records.
        ------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (6,0,[55,57]),
                (Command.set([64,65]))],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  

    def update_o2m_rec_inv(self):
        
        """
        This method is used to update existing O2M records for inverse method.
        ----------------------------------------------------
        @param self: object pointer
        """  
          
        new_rec =  {
            'crop_ids':[
                (1,7,{'govt_add':0}),
                ],
            
        } 
        new_crop = self.write(new_rec)
        print("O2M UPDATED",new_crop)  
    
    def read_spec_rec(self):
        
        """
        This method is used to read specific records.
        ----------------------------------------------------
        @param self: object pointer
        """  
          
        read_curr = self.read(['farmer_id','crop_ids','machine_ids','parent_id'])
        print("READ RECORDS",read_curr)  

    def read_spec_id(self):
        
        """
        This method is used to read M2O records id.
        ----------------------------------------------------
        @param self: object pointer
        """  
          
        read_id = self.read(['farmer_id'])
        print("READ RECORDS",read_id)  
