from odoo import models, fields

class SchoolActivity(models.Model):
    _name = 'school.activity'
    _description = 'Activities'

    name = fields.Char('Name')
    code = fields.Char('Code', size=5)
    color_index = fields.Integer('Color')
    # color_index field can be used to have the color assigned to the activities and can be seen on the tags widget.