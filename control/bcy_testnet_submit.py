# -*- coding: utf-8 -*-

from odoo import models
from blockcypher import send_faucet_coins
import time


class BCYTestnetSubmit(models.Model):

    _inherit = 'bcy.testnet.submit'

    def testnet_coin_submit(self):
        """
        Metodo para envio de coins na rede testnet
        :return: Hash da transacao realizada
        :rtype: str
        """
        try:
            datas = send_faucet_coins(address_to_fund=self.address,
                                      satoshis=self.satoshi,
                                      api_key=self.token)
        except:
            raise 'Coins nao enviados. Verifique o endereco e token informados.'
        tx_hash = datas.get('tx_ref')
        self.write({'name': self.name, 'state': 'D',
                    'date_time': time.strftime('%Y-%m-%d %H:%M:%S')})
        return tx_hash
