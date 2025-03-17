# This is the model file where we will define our models.
# We import the models(py file / module), fields(py file / module) from odoo directory)
from odoo import models, fields


# To create a model you need to create a class which will be child of models.Model (Inherited from models.Model)
# The naming convention is camelcase where only the first letter will be capital the remaining will be small.
# Incase if there are two words the first letter of each word will be capital others will remain small.
# For e.g. SchoolStudent

class SchoolStudent(models.Model):
    _name = 'school.student'
    # technical name of the model
    # This will be the name of the model which will be used to fetch the objects
    # It will also be used to create relational fields in other models.
    # It is also responsible to define the table's name in the database.
    # If the model name is school.student the table's name will be school_student  ('.' will be replaced by '_').
    # This will also be used to create views and action


    _description = 'Students'
    # This is the functional name of the model

    # _table = 'student_student'
    # # Instead of the table name given by _name if you want to give your own name you can mention that name here. This will be used as table's name if given.

    _auto = True
    # This is an attribute of model which decides whether the table should be automatically created or not.
    # By default it will be always true for models so we don't need to create the tables manually.

    # _order = '<field>' or '<field> desc'
    # _order is used to sort the records in the views based on the field mentioned.
    # if desc is used after the field it sorts in descending order else ascending order.

    # _rec_name = <field>
    # _rec_name stands for Recognized Name of the model.
    # By default name field is used for it. But if there is no name field we can assign any other field as recognized name for the model.


    # _sql_constraints
    # This will be used to add constraints in the database table.

    # _inherit
    # Will be used for Conventional Inheritance

    # _inherits
    # This will be used for Delegation Inheritance.

    # Adding Fields

    # <field_name> = fields.<fieldClass>(<params>)
    # Technically creating an object of the field's Class
    name = fields.Char(string='Name', required=True, index=True, size=64, translate=True)  # Creating an object of Char class having name as the field name and Name as Label
    # Char in Odoo VARCHAR  in PSQL
    # Field Attribute string is for Label of the Fields.
    # Field attribute required is used to make the field to be mandatory.
    # When you add required attribute from python it adds a NOT NULL constraint on the field in the database table.
    # Field attribute index is used to add an index on the field in the database.
    # Field attribute size is used only with Char field and restricts no of letters to be stored in the field
    # Field attribute translate is used for translation of the values in different languages.
    # The translate attribute works with Char, Text and Html fields only.
    active = fields.Boolean('Active', default=True)
    # Bool in Odoo boolean in PSQL
    # Field attribute default is used to provide default values in the field
    # roll_no = fields.Integer('Roll No', group_operator='avg')
    roll_no = fields.Integer('Roll No', aggregator='avg')
    # Integer in Odoo Integer in PSQL
    # group_operator attribute has 4 options sum,avg,min and max.
    # group_operator is DEPRECATED IN V18 USE aggregator instead everything else is the same.
    # The default one is sum.
    fees = fields.Float('Fees', default=1500.00, aggregator='min')
    # Float in Odoo Double Precision in PSQL
    notes = fields.Text('Notes', help="This field is used to put internal notes on the student")
    # Text in Odoo Text in PSQL
    # help field attribute is used to describe the field's usage or adding a tooltip.
    template = fields.Html('Template', readonly=True)
    # Html in Odoo Text in PSQL - (Stores HTML Code in Text in Table)
    # readonly field attribute is used to make the field to be readonly and uneditable.
    birthdate = fields.Date('Birthdate', default=fields.Date.today())
    # Date in Odoo Date in PSQL
    # fields.Date.today() gives you the current date
    login_time = fields.Datetime('Login Time', default=fields.Datetime.now())
    # fields.Datetime.now() gives you the current timestamp (date and time)
    # Datetime in Odoo Timestamp without Timezone in PSQL
    # In selection field we would give multiple options out of which one can be selected.
    # Basically it will be a dropdown field.
    # So here the options can be given as a list of tuple.
    # Each tuple will have exactly two elements.
    # First element will be the value which will be stored in the table.
    # Second element will be the value displayed in the field.
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    # Selection in Odoo Varying Character in PSQL
    # selection field attribute is used to provide the selection list of tuple in a Selection field

    # PRE-DEFINED FIELDS / MAGIC FIELDS
    # There are 5 fields which are pre-defined and automatically created.
    # id, create_uid, write_uid, create_date, write_date

    # The first field is 'id' is the primary for all the model's tables for Odoo.
    # It is an integer field which has auto values filled.

    # The second field is 'create_uid' (The User's ID who created the Record)
    # It is a Many2one field (res.users) in Odoo (Foreign Key in PSQL) to the res_users table

    # The third field is 'write_uid' (The user's ID who updated the record lastly)
    # It is a Many2one field (res.users) in Odoo (Foreign Key in PSQL) to the res_users table

    # The fourth field is 'create_date' (When the record was created)
    # This is a timestamp without timezone field and stores date and time when the record was created.

    # The fifth field is 'write_date' (When the record was updated lastly)
    # This is a timestamp without timezone field and stores date and time when the record was updated lastly.

    password = fields.Char('Password')
    email = fields.Char('Email')
    website = fields.Char('Website')
    phone = fields.Char('Mobile')
    in_time = fields.Float('In Time')
    out_time = fields.Float('Out Time')
    priority = fields.Selection([(str(ele),str(ele)) for ele in range(0,6)], 'Priority')
    # priority = fields.Selection([('0','0'),('1','1'),('2','2'),('3','3')], 'Priority')


    # RELATIONAL FIELDS

    # MANY2ONE
    # standard_id = fields.Many2one('school.standard', 'Standard')
    # Many2one is a Many to one relation between two models where multiple records from one model are linked to one record of another model.
    # Here in our case we have an m2o relation from students to standard depicting many students can study in one standard.
    # There are certain rules for M2O field.
    # First is the name of the M2O field must have a postifx _id. So if it is for standard we have mentioned standard_id.
    # The first attribute will be always the comodel name with which we are creating the relation. In our case it is school.standard
    # The second attribute is string which is the label of the field.
    # standard_id = fields.Many2one(comodel_name='school.standard', string='Standard', ondelete='set null')
    # ondelete is an attribute which can be used with many2one field only.
    # This is already a concept in the SQL with the Foreign key.
    # ondelete has 3 values set null, restrict and cascade.
    # This comes in picture when you try to delete a record that is linked in another table as foreign key value.
    # SET NULL is the default value and it means that if you delete a record from the table in the other table where it was set as a foreign key the value will become null.
    # For e.g. If you delete a standard it will set the Standard's value in student as null.
    standard_id = fields.Many2one(comodel_name='school.standard', string='Standard', ondelete='restrict')
    # RESTRICT will not allow to delete the record if the id is stored in the foreign key of another table.
    # For e.g. If you try to delete a standard but if it is already used in students the system will not allow you to delete it.
    # CASCADE will allow to delete the record even if it is stored in the foreign key of another table but it will also delete those records which have this value in foreign key.
    # For e.g. If you have marks related to student and you try to delete student, it will also delete their marks as well.
    # delegate = True attribute is used for Delegate Inheritance.

    # ONE2MANY
    # One2many is a One to Many relation between two models where one record is linked to multiple records of another model.
    # In our case we have a relation between student and marks depicting one student can have multiple marks.
    # For creating One2mnay field we will have the naming convention with name and postfix _ids.
    # The first attribute is the name of the comodel with which we are creating the relation.
    # The second attribute is the inverse_name which is the name of the many2one field in the opposite model for this model.
    # In our case there must be a Many2one field in the student.marks model for student called student_id.
    # The third attribute is the label of the field
    marks_ids = fields.One2many(comodel_name='student.marks', inverse_name='student_id', string='Marks')
    # One2many fields are not stored in the database table of the main model (Student in our case).
    # They are stored in the opposite table(student_marks) and we have the reference with the inverse_name field (student_id)

    # MANY2MANY
    # Many2many is a Many to many relation between two models where one ore more records are linked to one or more records of another model.
    # In our case we have a relation between student and activity depicting multiple students can do multiple activities.
    # For creating Many2many field we will have the naming convention with name and postfix _ids.
    # For M2M the first attribute is the comodel name with which we are going to create the relation.
    # You can then directly add string as the other attribute as well.
    # activity_ids = fields.Many2many('school.activity', string='Activities')
    # Many2many fields are not stored in teh databse table of the main model (Student in our case).
    # M2M creates a lookup table named with the both tables and postfixed with _rel.
    # For e.g. in our case our table name is school_student and the comodel is school_activity so it creates a lookup table called comodel_table_name + _current_model_table_name + _rel
    # In our case the lookup table created is school_activity_school_student_rel
    # This table contains exactly two fields which are foregin keys to my current model and the comodel.
    # The name of the fiels are taken as current_model's table name + _id and comodel's table name + _id.
    # In our case they are school_activity_id and school_student_id
    activity_ids = fields.Many2many(comodel_name='school.activity',relation='act_stud_rel',column1='stud_id',column2='act_id',string='Activities')
    # So if you want to explicitly give the names to the lookup table and the columns in the lookup table you can use the params in the following wya.
    # First parameter is the comodel name no change here and will be the name of the model with which we are creating the relation.
    # second parameter is the relation which is the name of the lookup table to be created.
    # third parameter is the name of the foreign key to current model's table. In our case stud_id for school_student.
    # fourth parameter is the name of the foreign key to the comodel's table. In our case act_id for school_activity.
    # fifth parameter is the string which is the label of the field.

    # domain is another field attribute used to filter the records and can be used with all the above 3 relational fields.
    # context is another field attribute that is used to pass certain parameters to the relational field. context is a standard dictionary which passes throughout the flow.
    # check_company attribute is used in case of multi-company environment.

    #REFERENCE
    # Reference field is a combination of Selection and Many2one field
    # The first parameter is a list of tuples where each tuple has exactly two elements just like a selection field.
    # Here in the reference field it is mandatory that the first element of the field is a model's name.
    # Second element can be any string referring to the model.
    # The second parameter is the label of the field.
    reference = fields.Reference([('res.users','Users'),('res.partner','Partner / Contact'),('school.student','Student')], string='Reference')
    # In the databse table the type of the field is varchar.
    # Depicting the combination of two fileds Selection and Many2one it stores information combining both.
    # Selection stores the key or first element in our case it is the name of the model.
    # Many2one stores the id of the record which is selected.
    # So it stores <model_name> + ',' + <id of the selected record>


    #OTHER FIELDS

    #MONETARY
    currency_id = fields.Many2one('res.currency', 'Currency')
    # res.currency is the model which stores all the currencies
    annual_fee = fields.Monetary(currency_field='currency_id',string='Annual Fee', aggregator='max')
    # Monetary field is used for amount that is related to an amount and it is always linked with currency.
    # the first attribute currency_field willl be the name of the currency field in our case currency_id is the M2O field for res.currency.
    # the second attribtue is the label of the field.

    # BINARY
    file_name = fields.Char('File Name')
    # The file_name is a char field which will be used to store the name of the file.
    doc = fields.Binary('Document')
    # Binary field is used to upload a document in the system.
    # This field is not created in the table in the databsae.
    # It stores the file on the filestore.

    # IMAGE
    photo = fields.Image('Photo')
    # Image field is derived from Binary and stores an image.