from odoo import models,fields,api

class FarmCrop(models.Model):
    _name = 'farm.crop'
    _description = 'farm crop'

    name = fields.Char('Crop Name')
    time = fields.Char('Growing Time (In Months)')
    crop_type = fields.Selection([('monsoon','Monsoon Season'),('winter','Winter Season'),('short','Short Season')],string='Type Of Crop')
    code = fields.Char(string='Code',size=4)
    farm_id = fields.Many2one(comodel_name='farm.model',string='Farm Code',domain="['!',('code','ilike','n%')]")
    cost = fields.Float('Cost (Rs.)')
    govt_add = fields.Float("Government's Profit Margin (%)")
    mrkt = fields.Float("Market's Profit Margin (%) ")

    govt_price = fields.Float(compute='_calc_govt_price', string='Government Price (Rs.)', inverse='_set_govt_price')
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

    def print_records(self):    

        self.env.cr.execute("UPDATE farm_crop SET name='peanut' WHERE id=6")
        res_1 = self.env.cr.fetchone()
        res_all = self.env.cr.fetchall()

        print("update successfull !!")   

        self.env.cr.execute("SELECT * from farm_crop") 
        res_1 = self.env.cr.dictfetchone()

        print(res_1)

    def print_dict_records(self):      

        self.env.cr.execute("SELECT * from farm_crop") 
        res_1 = self.env.cr.dictfetchone()

        print(res_1) 

    def print_dict_records_all(self):      

        self.env.cr.execute("SELECT * from farm_crop") 
        res_1 = self.env.cr.dictfetchall()

        print(res_1)           
    
    def del_records(self):    

        self.env.cr.execute("delete from farm_crop WHERE id=6")

        print("deleted successfully !!")   

        self.env.cr.execute("SELECT * from farm_crop") 
        res_1 = self.env.cr.dictfetchone()

        print(res_1)

    def print_data(self):    

        uid = self.env.uid
        print(uid)
        user = self.env.user
        print(user)
        ctxt = self.env.context
        print(ctxt)
        comp = self.env.company
        print(comp)
        comps = self.env.companies
        print(comps)
        lang = self.env.lang
        print(lang)

    def list_modl(self):
        
        rel_obj = self.env['farm.model']
        print(rel_obj)
        data_model = self.env.keys()
        data_obj = self.env.values()
        data_all = self.env.items()
        print(list(data_model))   
        print(list(data_obj))   
        print(list(data_all))   

    def print_from_xml_id(self):
        view_xml_id = self.env.ref('farm_module.view_crop_tree')   
        print("VIEW",view_xml_id) 
        act_xml_id = self.env.ref('farm_module.action_crop')   
        print("ACTION",act_xml_id) 
        menu_xml_id = self.env.ref('farm_module.menu_crop_info')   
        print("MENU",menu_xml_id) 

    def print_rec_add_data(self):

        grp_data = self.env.ref('farm_module.grp_farm_admin')
        print(grp_data)

        access_data = self.env.ref('farm_module.access_farm_farmer')
        print(access_data)

        user_data = self.env.ref('base.user_admin')
        print(user_data)

        comp_data = self.env.ref('base.main_company')
        print(comp_data)      


    # ORM Methods

    def create_rec(self):
        """
        This method is used to create records using create method
        ---------------------------------------------------------
        @params self: Object pointer

        """

        new_rec =  {
            'name':'peanut',
            'crop_type':'monsoon',
            'farm_id' : 4,
            'code':'PNUT',
            'cost':'8900.0',
            'govt_add':'56.0',
            'mrkt': '78.0'
        }   
        
         
        new_crop = self.create(new_rec)
        print("Record Created",new_crop)

    def create_rec_diff(self):
        """
        This method is used to create record in another model using create method
        ---------------------------------------------------------
        @params self: Object pointer

        """

        farmer_obj = self.env['farm.farmer']

        new_rec =  {
            'name':'Shailesh Chaudhari',
            'age':48,
            'gender' : 'male',
            'mo_no':'9909699774',
        }   
        
         
        new_farmer = farmer_obj.create(new_rec)
        print("Record Created",new_farmer)    

    # write() method 

    def update_rec(self):
        """
        This method is used to update records using write method
        ---------------------------------------------------------
        @params self: Object pointer

        """

        new_rec =  {
            'name':'peanut',
            'crop_type':'monsoon',
            'farm_id' : 4,
            'code':'PNUT',
            'cost':'8900.0',
            'govt_add':'56.0',
            'mrkt': '78.0'
        }   
        
         
        new_crop = self.write(new_rec)
        print("Record Created",new_crop)

    def update_rec_diff(self):
        """
        This method is used to update records of another model using write method
        ---------------------------------------------------------
        @params self: Object pointer

        """
        farm_obj = self.env['farm.model'].search([])

        for farm in farm_obj:    

            new_rec =  {
                'farm_type':'medium'
            }   
                
            farm_updated = farm.write(new_rec)
            print("Record Created",farm_updated)

    def _set_govt_price(self):
        """
        This is an inverse method which will be called when you try to use compute field in the write method.
        -----------------------------------------------------------------------------------------------------
        @param self: object pointer / recordset
        """

        for crop in self:
            if crop.govt_add == 0.0:
                crop.govt_add = 35.0
                crop.govt_price = crop.cost + (crop.cost * crop.govt_add)/100

    def read_group_rec(self):
        """
        This method is used to read the group of records.
        -------------------------------------------------
        @param self: object pointer / recordset
        """

        res = self.read_group([], fields=['cost'], groupby=['crop_type','time'], orderby='crop_type',lazy=False)
        print("SINGLE GROUP", res)

