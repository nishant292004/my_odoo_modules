{
    'name':'School Management', # Functional Name of the module
    'summary':'This module will be used for School Management', # Short summary of module
    'description':"""This modules is used to manage School Information.
    We will manage the Student Information""", # Detailed Description of Module
    'version':'1.0', # Version of module
    'category':'School', # Category of module
    'author':'Skyscend Busienss Solutions Pvt. Ltd.', # Author of the module / app
    'website':'www.skyscendbs.com', # Website of the Author
    'depends': ['base'], # The parent modules on which your module / app depends on. At least base must be there if not depending on any other module(s).
    'data':[
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/standard_view.xml',
        'views/subject_view.xml',
        'views/marks_view.xml',
        'views/activity_view.xml',
    ], # Data a list containing all your xml and csv files. The sequence is very important. First we keep the security file where groups are created. Then the access rights where groups will be used and finally the views file.
    'sequence':10, # This will be the sequence of module to be displayed on the Apps menu
    'auto_install': False, # IF True then it will be automatically installed if all the parent modules are already installed.
    'installable': True, # Whether you can install this module or not. False only if still in development.
    'application': True, # TO decide whether it's an application or just a supporting addon module to add some feature in the app.
    'license': 'LGPL-3', # License of the module
}


# To run the server we go to odoo directory and run the command ./odoo-bin
# To give addons path for custom modules we use the parameter --addons or --addons-path
# The syntax is ./odoo-bin --addons addons/,odoo/addons,<path_of_custom_modules>
# Whenever you make changes in the Python file you need to restart the server.
# To restart use Ctrl + C to stop the server and then restart it.
# Whenever you make changes in XML or CSV file you need to upgrade the module.
# You can upgrade the module from the Apps from GUI.
# You can also upgrade the module from terminal using the params -d <database_name> and -u <module_name>
# The syntax would be ./odoo-bin --addons addons/,odoo/addons,<path_of_custom_modules> -d <db_name> -u <module_name>

