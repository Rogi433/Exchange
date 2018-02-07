"""
Esse arquivo deve controlar os metodos de criar novas trades e exibi-las
Toda vez que uma nova oferta for criada, ira se iniciar tambem uma busca pelas outras ofertas e ver se eh possivel realizar
uma Tradel. Isso significa que alguma funcao dentro da pasta "offer" vai chamar funcoes daqui para ver se tem como realizar uma trade
"""

from exchange.offer.model import Offer
import exchange.trade.model as trade_model

TRADES = trade_model.DATA


def trade(offer):
    new_trade = None

    if offer.side == 'B':
        if Offer.SELL and Offer.SELL[0].price <= offer.price:
            if Offer.SELL[0].quantity == offer.quantity:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.SELL[0], offer.user, Offer.SELL[0].user, Offer.SELL[0].price,
                                              offer.quantity)
                Offer.SELL.pop(0)
                TRADES.append(new_trade)
            elif Offer.SELL[0].quantity <= offer.quantity:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.SELL[0], offer.user, Offer.SELL[0].user, Offer.SELL[0].price,
                                              Offer.SELL[0].quantity)
                TRADES.append(new_trade)
                offer.quantity = offer.quantity - Offer.SELL[0].quantity
                Offer.SELL.pop(0)
                trade(offer)
            else:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.SELL[0], offer.user, Offer.SELL[0].user, Offer.SELL[0].price,
                                              offer.quantity)
                TRADES.append(new_trade)
                Offer.SELL[0].quantity = Offer.SELL[0].quantity - offer.quantity
        else:
            Offer.BUY.append(offer)
            Offer.BUY.sort_buy()

    else:
        if Offer.BUY and Offer.BUY[0].price >= offer.price:
            if Offer.BUY[0].quantity == offer.quantity:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.BUY[0], offer.user, Offer.BUY[0].user, Offer.BUY[0].price,
                                              offer.quantity)
                Offer.BUY.pop(0)
                TRADES.append(new_trade)
            elif Offer.BUY[0].quantity <= offer.quantity:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.BUY[0], offer.user, Offer.BUY[0].user, Offer.BUY[0].price,
                                              Offer.BUY[0].quantity)
                TRADES.append(new_trade)
                offer.quantity = offer.quantity - Offer.BUY[0].quantity
                Offer.BUY.pop(0)
                trade(offer)
            else:
                new_trade = trade_model.Trade(len(TRADES)+1, offer, Offer.BUY[0], offer.user, Offer.BUY[0].user, Offer.BUY[0].price,
                                              offer.quantity)
                TRADES.append(new_trade)
                Offer.BUY[0].quantity = Offer.BUY[0].quantity - offer.quantity
        else:
            Offer.SELL.append(offer)
            Offer.SELL.sort_sell()

    return new_trade
