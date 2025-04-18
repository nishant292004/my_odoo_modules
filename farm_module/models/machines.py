from odoo import models,fields

class FarmMachines(models.Model):
    _name='farm.machines'
    _description = 'farmer of the farm'

    name = fields.Char("Machine Name")
    code = fields.Char("code",size=4)
    description = fields.Text("Description")
    currency_id = fields.Many2one('res.currency','Currency')
    price = fields.Monetary(currency_field='currency_id',string='Machine price')
    reference = fields.Reference([('farm.model','Farm'),('farm.farmer','Farmer'),('farm.crop','Crop')], string='Reference')
    file_name = fields.Char('File Name')
    doc = fields.Binary('Machine Specification')
    photo = fields.Image('Image')
    extra_info =fields.Html('Additional Information')

    def browse_rec(self):
        """
        This is a method used to demonstrate browse() method
        -----------------------------------------------------
        @param self: object pointer
        """
        single_rec = self.browse(5)
        print("SINGLE RECORD", single_rec)
    
    def browse_rec_multi(self):
        """
        This is a method used to browse multiple records
        -------------------------------------------------
        @param self: object pointer
        """
        multi_rec = self.browse([2,4,6])
        print("MULTIPLE RECORDS", multi_rec)

    def browse_rec_one_diff(self):
        """
        This is a method used to browse single record from different model
        ------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop']
        single_rec = crop_obj.browse(1)
        print("SINGLE RECORD", single_rec)

    def browse_rec_multi_diff(self):
        """
        This is a method used to browse multiple records from different model
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop']
        multi_rec = crop_obj.browse([2,4,7])
        print("MULTIPLE RECORDS", multi_rec)

    def read_rec(self):
        
        """
        This method is used to read records.
        ------------------------------------
        @param self: object pointer
        """  
          
        read_machines = self.read()
        print("READ RECORDS",read_machines)  
    
    def read_spec_rec(self):
        
        """
        This method is used to read specific records.
        ---------------------------------------------
        @param self: object pointer
        """  
          
        read_machines = self.read(['name','code','reference'])
        print("READ RECORDS",read_machines)  

    def read_diff_rec(self):
        
        """
        This method is used to read records of different model.
        ------------------------------------------------------
        @param self: object pointer
        """  
        

        crop_obj = self.env['farm.crop']
        multi_rec = crop_obj.browse([2,4,7])
        read_rec = multi_rec.read()
        print("READ RECORDS",read_rec)  

    def dupl_rec(self):
        """
        This is a button's method used to demonstrate copy() method
        -----------------------------------------------------------
        @param self: object pointer
        """

        copy_rec =self.copy()
        print("COPY REC",copy_rec)

    def dupl_rec_create(self):
        """
        This is a button's method used to copy record without using copy
        ----------------------------------------------------------------
        @param self: object pointer
        """
        for rec in self:
            copy_rec ={'name':rec.name+'(copy)'}
            rec.create(copy_rec)
            print("COPY REC")
    

    def dupl_rec_multi(self):
        """
        This is a method used to duplicate multiple records
        ---------------------------------------------------
        @param self: object pointer
        """
        multi_recs = self.browse([4,5,6])
        copy_rec =multi_recs.copy()
        print("COPY REC",copy_rec)

    def dupl_rec_ident(self):
        """
        This is a method used to duplicate multiple records such that we can differentiate it
        -------------------------------------------------------------------------------------
        @param self: object pointer
        """
        for rec in self:
            default = {
                'name': rec.name + ' (Copy)'
            }
            new_rec = rec.copy(default=default)
            print("NEW REC", new_rec)

    def delete_rec(self):
        """
        This is a method used to delete the record from the current model
        -----------------------------------------------------------------
        @param self: object pointer
        """
        cur_rec = self.browse(12)
        cur_rec.unlink()
        print("RECORD DELETED")

    def delete_multi_rec(self):
        """
        This is a method used to delete the multiple records from the current model
        ---------------------------------------------------------------------------
        @param self: object pointer
        """
        cur_rec = self.browse([9,10,11])
        cur_rec.unlink()
        print("RECORDS ARE DELETED")    

    def delete_multi_rec_diff(self):
        """
        This is a method used to delete the multiple records from the different model
        -----------------------------------------------------------------------------
        @param self: object pointer
        """
        crop_obj = self.env['farm.crop']
        cur_rec = crop_obj.browse([64,65])
        cur_rec.unlink()
        print("RECORDS ARE DELETED FROM OTHER MODEL")  

    def search_rec(self):
        """
        this method is used to fetch all thee the current model's record
        ----------------------------------------------------------------
        @param self: object pointer
        """
        all_recs = self.search(domain=[],order='name desc')
        print("ALL RECORDS",all_recs)                  

    def search_spec_rec(self):
        """
        this method is used to fetch the specific record for current model 
        ------------------------------------------------------------------
        @param self: object pointer
        """
        all_recs = self.search([('description','=',False)])
        print("ALL RECORDS",all_recs)

    def search_spec_rec_diff(self):
        """
        this method is used to fetch the specific record for another model 
        ------------------------------------------------------------------
        @param self: object pointer
        """
        farm_obj = self.env['farm.model']
        all_recs = farm_obj.search(domain=[('farm_type','=','large')],offset= 2,limit=5 ,order='est_date desc')
        print("ALL RECORDS OF FARM MODEL",all_recs)                                        

    def search_count_record(self):
        """
        This is a method used to count() the records
        --------------------------------------------
        @param self: object pointer
        """
        all_recs = self.search_count([])
        print('ALL', all_recs)
        desc_records = self.search_count([('description','=',False)])
        print("NOT DESCRIPTION RECORDS", desc_records)

    def search_count_record_diff(self):
        """
        This is a method used to count() the records of another model
        -------------------------------------------------------------
        @param self: object pointer
        """
        farm_obj = self.env['farm.model']
        all_recs = farm_obj.search_count([])
        print('ALL FARM RECORDS', all_recs)

    def search_read_record(self):
        """
        This is a method used to search and read the records of current model
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        farm_obj = self.env['farm.model']        
        all_recs = farm_obj.search([('farm_type','=','large')])
        print("SEARCH",all_recs)
        res_recs = all_recs.read()
        print('ALL RECORDS', res_recs)
        
    def search_user_id(self):
        """
        This is a method used to search the id of user who created the record
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        for rec in self:

            user_id = rec.create_uid
            print(user_id)
