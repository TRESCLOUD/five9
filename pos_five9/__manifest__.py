# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Five9 TPV',
    'version': '1.0',
    'category': 'POS',
    'author': 'TRESCLOUD CIA. LTDA.',
    'maintainer': 'TRESCLOUD CIA. LTDA.',
    'website': 'http://www.trescloud.com',
    'description': '''Implementa en el TPV las siguientes características de Five9:
                        * Muestra un cliente cuando se accede desde url especifica''',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        'views/js_files_link.xml',
        # Views
        'views/res_partner_view.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False
}
