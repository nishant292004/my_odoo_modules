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
        -------------------------------------------------------------
        @param self: object pointer
        """
        single_rec = self.browse(5)
        print("SINGLE RECORD", single_rec)
    