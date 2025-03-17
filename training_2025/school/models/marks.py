from odoo import models, fields, api
# we imported api to use depends decorator for compute attribute of the field.

class StudentMarks(models.Model):
    _name = 'student.marks'
    _description = 'Student Marks'

    student_id = fields.Many2one('school.student', 'Student', ondelete='cascade')
    # ondelete='cascade' will delete the records in this table if you delete the record linked to student_id.
    # So if you delete the studnet their related marks will also get deleted.
    subject_id = fields.Many2one('school.subject', 'Subject')
    subject_code = fields.Char(related='subject_id.code', string='Subject Code')
    # related attribute is used to fetch the field from a relational field's record.
    # For e.g. IF I want to fetch the subject's code from the selected subject I can use related.
    # The syntax of using related is related=<relational_field>.<field of relational model of the field>.
    # e.g. subject_id.code
    # By default the fields with related attribute are not stored in the database table.
    # The related fields are readonly fields by default as they're fetching the information from another record.
    # Similar to compute if you want to forcefully store these fields you can using store=True
    total_marks = fields.Float('Total Marks')
    pass_marks = fields.Float('Passing Marks')
    obt_marks = fields.Float('Obtained Marks')
    perc = fields.Float(compute='_calc_perc', string='Percentage(%)', store=True)
    # compute attribute is used when you want to compute the value of a field.
    # The value to compute is a method which will calculate the value of this field.
    # By default the fields with compute attribute are not stored in the table.
    # using the store=True attribute you can store the field which is having compute attribute.
    # If you're using store=True, you must use @api.depends to call the method as that is the only way the compute method will be called.
    # For storable fields compute methods don't get called on save and read.
    result = fields.Selection([('pass','Pass'),('fail','Fail')], compute='_calc_result', string='Result')

    # TODO: when we have 'compute' we can also use 'search' and 'inverse' attribute which we will see when we go through search and write methods.

    @api.depends('total_marks','obt_marks')
    def _calc_perc(self):
        """
        This method is used to calculate the percentage based on the total marks and obtained marks
        -------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        # This method is a compute field method.
        # This method must set the value of the field for which it is called even with a 0 or False value as per the type.
        # This method gets called when you save the record or when you open the record(read the record).
        # If @api.depends is mentioned the method gets called when you change the fields mentioned in the decorator api.depends
        # So instead of method being called only on save and read it also gets called when you change the values on field even before saving.
        print("SELF", self)
        # Self is a recordset containing one or more records.
        # For e.g. student.marks(10, 11, 12)
        # The recordset is defined as the name of the model and then in bracket the ids of the selected records.
        # The recordset can be blank, can have only one record or can also have multiple records.
        # Using for loop you can iterate through a record set and get single record recordset.
        for mark in self:
            # To access the fields you must have a single record recordset.
            print("MARK",mark)
            # To access the field you use <record_set>.<field_name>
            # For e.g. mark.subject_id as shown below
            print("MARK SUBJECT", mark.subject_id)
            # To assign the value to the field we will use <record_set>.<field_name> = <value>
            if mark.total_marks:
                mark.perc = (mark.obt_marks * 100.00) / mark.total_marks
            else:
                mark.perc = 0.0


    def _calc_result(self):
        """
        This method will calculate the result for the subject based on obtained marks and passing marks
        -----------------------------------------------------------------------------------------------
        @param self: object pointer
        """
        for mark in self:
            if mark.obt_marks >= mark.pass_marks:
                mark.result = 'pass'
            else:
                mark.result = 'fail'