# -*- coding: utf-8 -*-

from odoo import models
from blockcypher import get_transaction_details


class BCYTestnetToReceive(models.Model):

    _inherit = 'bcy.testnet.to.receive'

    def testnet_coin_receive(self):
        """"
        Metodo para recebimento de coins na rede testnet
        :return: Hash da transacao realizada
        :rtype: str
        """
        try:
            datas = get_transaction_details(tx_hash=self.tx_hash,
                                            coin_symbol='bcy')
        except:
            raise 'Hash da transacao nao identificado.'
        vals = {'name': datas.get('hash')}
        if self.get('confirmations') >= 2:
            vals.update({'confirmation': datas.get('confirmations'),
                         'data_time': str(datas.get('confirmed')),
                         'state': 'D', 'satoshi': datas.get('outputs')[0].get('value')})
        self.write(vals)
        return datas.get('hash')
