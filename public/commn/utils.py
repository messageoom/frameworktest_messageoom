#coding=utf-8
__author__ = 'Kal-W'
import random
import numpy as np
import decimal
class Utils(object):
#    def __init__(self,now_price=None):
#        self.now_p = now_price

    def limit_price(self,now_price):
        """ Generate the price when adding shares"""
        stockPrice = []

        limit_up_price  = "%.2f" % (now_price + (now_price * 0.1))
        stockPrice.append(limit_up_price)
        limit_down_price = "%.2f" % (now_price - (now_price * 0.1))
        stockPrice.append(limit_down_price)
        first_buying_rate_arry = np.arange(now_price - (now_price * 0.01),now_price + (now_price * 0.01),0.01)
        first_buying_rate = float("%.2f" % random.choice(first_buying_rate_arry))
        stockPrice.append(first_buying_rate)
        second_selling_rate_arry = np.arange(first_buying_rate - (first_buying_rate * 0.01), first_buying_rate, 0.01)
        second_selling_rate = float("%.2f" % random.choice(second_selling_rate_arry))
        stockPrice.append(second_selling_rate)
        fist_win_rate_arry = np.arange(first_buying_rate + 0.02,now_price + (now_price * 0.05))
        first_win_rate = float("%.2f" % random.choice(fist_win_rate_arry))
        stockPrice.append(first_win_rate)
        second_win_rate_arry = np.arange(now_price + (now_price * 0.05),now_price + (now_price * 0.1))
        second_win_rate = float("%.2f" % random.choice(second_win_rate_arry))
        stockPrice.append(second_win_rate)
        first_lose_rate_arry = np.arange(now_price - (now_price * 0.015),now_price)
        first_lose_rate = float("%.2f" % random.choice(first_lose_rate_arry))
        stockPrice.append(first_lose_rate)
        second_lose_rate_arry = np.arange(now_price - (now_price * 0.02),now_price - (now_price * 0.016))
        second_lose_rate = float("%.2f" % random.choice(second_lose_rate_arry))
        stockPrice.append(second_lose_rate)

        return stockPrice
