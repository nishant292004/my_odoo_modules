from odoo import fields, models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subjects'

    name = fields.Char('Name')
    code = fields.Char('Code', size=4)

