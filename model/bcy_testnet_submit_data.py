# -*- coding: utf-8 -*-

from odoo import models, fields


class BCYTestnetSubmit(models.Model):
    _description = 'Classe para envio de fracoes de moedas ' \
                   'na rede testnet'
    _name = 'bcy.testnet.submit'

    name = fields.Char(string='TX Hash', size=64, readonly=True)
    token = fields.Char(string='Token', size=32, required=True,
                        attrs="{'readonly': [('state', '=', 'D')]}")
    state = fields.Selection([('P', 'Pending'), ('D', 'Done')],
                             string='Status', size=1,
                             default='P', readonly=True)
    date_time = fields.Datetime(string='Date/time', readonly=True)
    satoshi = fields.Integer(string='Satoshi', required=True,
                             attrs="{'readonly': [('state', '=', 'D')]}")
    address = fields.Char(string='Address', size=34, required=True,
                          attrs="{'readonly': [('state', '=', 'D')]}")
