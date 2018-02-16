"""
Esse arquivo deve controlar os metodos de criar novas trades e exibi-las
Toda vez que uma nova oferta for criada, ira se iniciar tambem uma busca pelas outras ofertas e ver se eh possivel
realizar uma Trade. Isso significa que alguma funcao dentro da pasta "offer" vai chamar funcoes daqui para ver se tem
como realizar uma trade.
"""

from exchange.offer.model import Offer
import exchange.trade.model as trade_model

TRADES = trade_model.DATA


def trade(offer):

    if offer.side == 'B':
        if Offer.SELL and Offer.SELL[0].price <= offer.price:
            if Offer.SELL[0].quantity == offer.quantity:
                quantity = offer.quantity
                offer.update_quantity(Offer.SELL[0].quantity)
                Offer.SELL[0].update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.SELL[0], Offer.SELL[0].price, quantity)
                Offer.SELL.pop(0)
                TRADES.append(new_trade)
                print('compra')

            elif Offer.SELL[0].quantity <= offer.quantity:
                quantity = Offer.SELL[0].quantity
                Offer.SELL[0].update_quantity(offer.quantity)
                offer.update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.SELL[0], Offer.SELL[0].price, quantity)
                TRADES.append(new_trade)
                Offer.SELL.pop(0)
                print('compra')
                trade(offer)

            else:
                quantity = offer.quantity
                offer.update_quantity(Offer.SELL[0].quantity)
                Offer.SELL[0].update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.SELL[0], Offer.SELL[0].price, quantity)
                TRADES.append(new_trade)
                print('compra')

        else:
            Offer.BUY.append(offer)
            Offer.BUY.sort_buy()
            print('arquiva na lita de Bids')

    else:
        if Offer.BUY and Offer.BUY[0].price >= offer.price:
            if Offer.BUY[0].quantity == offer.quantity:
                quantity = offer.quantity
                offer.update_quantity(Offer.SELL[0].quantity)
                Offer.BUY[0].update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.BUY[0], Offer.BUY[0].price, quantity)
                Offer.BUY.pop(0)
                TRADES.append(new_trade)
                print('venda')

            elif Offer.BUY[0].quantity <= offer.quantity:
                quantity = Offer.BUY[0].quantity
                Offer.BUY[0].update_quantity(quantity)
                offer.update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.BUY[0], Offer.BUY[0].price, quantity)
                TRADES.append(new_trade)
                Offer.BUY.pop(0)
                print('venda')
                trade(offer)

            else:
                quantity = offer.quantity
                offer.update_quantity(Offer.SELL[0].quantity)
                Offer.BUY[0].update_quantity(quantity)

                new_trade = trade_model.Trade(offer, Offer.BUY[0], Offer.BUY[0].price, quantity)
                TRADES.append(new_trade)
                print('venda')
        else:
            Offer.SELL.append(offer)
            Offer.SELL.sort_sell()
            print('arquiva na lista de Asks')

    return
