{
    'name':'Cars Management', # Functional Name of the module
    'summary':'This module will be used for Cars Management', # Short summary of module
    'description':"""This modules is used to manage Cars Information.
    We will manage the Cars Information""", # Detailed Description of Module
    'version':'1.0', # Version of module
    'category':'Cars', # Category of module
    'author':'Nishant', # Author of the module / app
    'depends': ['base'], # The parent modules on which your module / app depends on. At least base must be there if not depending on any other module(s).
    'data':[
        'security/car_security.xml',
        'security/ir.model.access.csv',
       'views/cars_view.xml',
       'views/engine_view.xml',
       'views/tagz_view.xml',
       'views/client_view.xml',
       'views/purchase_view.xml',
       

    ], # Data a list containing all your xml and csv files. The sequence is very important. First we keep the security file where groups are created. Then the access rights where groups will be used and finally the views file.
    'sequence':10, # This will be the sequence of module to be displayed on the Apps menu
    'auto_install': False, # IF True then it will be automatically installed if all the parent modules are already installed.
    'installable': True, # Whether you can install this module or not. False only if still in development.
    'application': True, # TO decide whether it's an application or just a supporting addon module to add some feature in the app.
    'license': 'LGPL-3', # License of the module
}
