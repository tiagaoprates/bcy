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
        'views/teste_view.xml',
        'views/action.xml',
        'views/menu.xml',
        'security/teste_group.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}
