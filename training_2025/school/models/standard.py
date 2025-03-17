from odoo import models, fields

class SchoolStandard(models.Model):

    _name = 'school.standard'

    _description = 'Standards'

    _rec_name = 'code'
    # Adding a recognized name filed instead of name it should display code.

    name = fields.Char('Name')
    code = fields.Char('Code', size=4)

