# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import ValidationError
from blockcypher import get_transaction_details


class BCYTestnetToReceiveControl(models.Model):

    _description = 'Classe para recebimento de fracoes de moedas ' \
                   'na rede testnet'
    _inherit = 'bcy.testnet.to.receive'

    @api.multi
    def testnet_receive_coin(self):
        """"
        Metodo para recebimento de coins na rede testnet
        :return: Hash da transacao realizada
        :rtype: str
        """
        try:
            datas = get_transaction_details(tx_hash=self.tx_hash,
                                            coin_symbol='bcy')
        except:
            raise ValidationError('Hash da transacao invalido ou nao '
                                  'identificado.')
        if datas.get('error'):
            raise ValidationError('Transacao nao encontrada.')
        vals = {'name': datas.get('hash')}
        if datas.get('confirmations') >= 2:
            vals.update({'confirmation': datas.get('confirmations'),
                         'date_time': str(datas.get('confirmed')),
                         'state': 'D',
                         'satoshi': datas.get('outputs')[0].get('value')})
        self.write(vals)
        return datas.get('hash')
