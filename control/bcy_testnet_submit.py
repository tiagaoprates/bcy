# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import ValidationError
from blockcypher import send_faucet_coins
import time


class BCYTestnetSubmitControl(models.Model):

    _description = 'Classe para envio de fracoes de moedas ' \
                   'na rede testnet'
    _inherit = 'bcy.testnet.submit'

    @api.multi
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
            raise ValidationError('Coins nao enviados. Verifique o endereco '
                                  'e/ou token informados.')
        tx_hash = datas.get('tx_ref')
        self.write({'name': tx_hash, 'state': 'D',
                    'date_time': time.strftime('%Y-%m-%d %H:%M:%S')})
        return tx_hash
