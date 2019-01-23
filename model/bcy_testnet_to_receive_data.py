# -*- coding: utf-8 -*-

from odoo import models, fields


class BCYTestnetToReceive(models.Model):
    _description = 'Classe para recebimento de fracoes de moedas ' \
                   'na rede testnet'
    _name = 'bcy.testnet.to.receive'

    name = fields.Char(string='Hash', size=64, readonly=True)
    tx_hash = fields.Char(string='TX Hash', size=64, required=True)
    state = fields.Selection([('P', 'Pending'), ('D', 'Done')],
                             string='Status', size=1,
                             default='P', readonly=True)
    date_time = fields.Datetime(string='Date/time', readonly=True)
    satoshi = fields.Integer(string='Satoshis', readonly=True)
    confirmation = fields.Integer(string='Confirmations', readonly=True)
