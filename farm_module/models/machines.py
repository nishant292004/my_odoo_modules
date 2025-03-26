from odoo import models,fields

class FarmMachines(models.Model):
    _name='farm.machines'
    _description = 'farmer of the farm'

    name = fields.Char("Machine Name")
    code = fields.Char("code",size=4)
    description = fields.Text("Description")
    