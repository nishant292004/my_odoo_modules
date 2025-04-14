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

    govt_price = fields.Float(compute='_calc_govt_price', string='Government Price (Rs.)')
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

    def       
