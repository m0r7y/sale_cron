# -*- coding: utf-8 -*-
{
    'name': "Tâches cron pour Pipeline",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ingenosya",
    'website': "http://www.ingenosya.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/cron_task_configuration.xml',
        'views/crm_lead_reminder.xml',
        'views/crm_lead_add_new_field.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,

}