# -*- coding: utf-8 -*-
{
    'name': "bcy",

    'summary': """Modulo de integracao ao testnet do BlockCypher.""",

    'description': """
        Permite enviar e receber fracoes de moedas na rede testnet
    """,

    'author': "Tiago Prates",

    'category': 'Test',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'view/bcy_testnet_submit_view.xml',
        'view/bcy_testnet_to_receive_view.xml',
        'view/action.xml',
        'view/menu.xml',
        'security/bcy_group.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}
