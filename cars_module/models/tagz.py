from odoo import models,fields

class CarTagz(models.Model):

    _name = 'cars.tagz'
    _description = 'Your own tagz for your cars'
    _rec_name = 'tag_name'


    tag_name = fields.Char('Tag Name', required=True)
    color_index = fields.Integer('color', required=True)
