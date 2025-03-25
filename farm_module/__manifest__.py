{
    'name':'Farm Management', 
    'summary':'This module will be used for Farm Management', 
    'description':"""This module will manage all the information of farming.""", 
    'version':'1.0', 
    'category':'Farming', 
    'author':'Nishant', 
    'depends': ['base'], 
    'data':[
        'security/farm_security.xml',
       'security/ir.model.access.csv',
       'views/farm_view.xml',
    ], 
    'sequence':10, 
    'auto_install': False, 
    'installable': True, 
    'application': True, 
    'license': 'LGPL-3', 
}
