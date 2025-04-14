from odoo import models,fields

class Farmer(models.Model):
    _name='farm.farmer'
    _description = 'farmer of the farm'

    name = fields.Char("Farmer's Name")
    age = fields.Integer(string="Age",aggregator='max')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string='Active' , default = True, invisible=True)
    mo_no = fields.Char("Mobile no.")
    no_of_farms = fields.Integer(compute="_calc_no_of_farms")
    farm_id = fields.Many2one(comodel_name='farm.model', string='Farm Code', ondelete="restrict")
    crop_ids = fields.Many2many(comodel_name='farm.crop',string="Types Of Crops")
    machine_ids = fields.Many2many(comodel_name='farm.machines',relation='machine_farmer_rel',column1='machines_id',column2='farmer_id',string="Machines used in farm")

    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.uid)
    comp_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company.id)
    lang_id = fields.Many2one('res.lang', 'language', default=lambda self:  self.env['res.lang'].search([('code', '=', 'en_US')], limit=1).id)
    currency_id = fields.Many2one('res.currency', 'Currency', default=lambda self: self.env.ref('base.USD').id)



    def print_name(self):

        print(self.name)

    def _calc_no_of_farms(self):

        farm_obj = self.env['farm.model']

        for farmer in self:
            farmer.no_of_farms = farm_obj.search_count([('farmer_id','=',farmer.id)])
