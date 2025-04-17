{
    'name':'Farm Management', 
    'summary':'This module will be used for Farm Management', 
    'description':"""This module will manage all the information of farming 
    related             activities. Like the information about farm ,farmers ,machines and crops. it will showcase all the data and the relations between different models.""", 
    'version':'1.0', 
    'category':'Farming', 
    'author':'Skyscend Business Solution Pvt. Ltd.', 
    'depends': ['base'], 
    'data':[
        'security/farm_security.xml',
       'security/ir.model.access.csv',
       'views/farm_view.xml',
       'views/crop_view.xml',
       'views/farmer_view.xml',
       'views/machine_view.xml',
    ], 
    'auto_install': False, 
    'installable': True, 
    'application': True, 
    'license': 'LGPL-3', 
}
