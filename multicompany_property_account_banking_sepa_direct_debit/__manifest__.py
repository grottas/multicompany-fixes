# Copyright 2018 Creu Blanca
# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Multi Company Property Account Banking SEPA Direct Debit',
    'version': '11.0.1.0.0',
    'summary': 'Account Company Properties',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'sequence': 30,
    'license': 'LGPL-3',
    'website': 'http://www.eficent.com',
    'depends': ['multicompany_property_account_banking_pain_base',
                'account_banking_sepa_direct_debit'],
    'data': [
        'views/res_company_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
