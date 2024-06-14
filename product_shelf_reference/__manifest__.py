{
    'name': 'Product Shelf Reference',
    'version': '16.0.0.0',
    'category': 'Inventory',
    'summary': 'Add a custom field in the product template to add shelf reference',
    'description': 'This module allows you to add a custom field in the product template to store the shelf reference for each product.',
    'author': 'Gerlin Matos',
    'depends': ['base','product'],
    'data': [
        'views/product_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}