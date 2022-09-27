import numpy as np
from py_vollib.black_scholes.implied_volatility import implied_volatility
from py_vollib.black_scholes.greeks.analytical import delta
import datetime as dt


def winddown(time):
    if time < dt.time(9, 30):
        return 0.7
    elif time < dt.time(9, 45):
        return 0.6
    elif time < dt.time(10, 30):
        return 0.5
    elif time < dt.time(11, 30):
        return 0.4
    elif time < dt.time(13):
        return 0.3
    elif time < dt.time(14, 30):
        return 0.25
    elif time < dt.time(15, 30):
        return 0.15
    elif time < dt.time(16):
        return 0.05
    else:
        return 0


def tte(start_time, end_time):
    trading_days = np.busday_count(start_time.date(), end_time.date())
    start_time_winddown = winddown(start_time.time())
    end_time_winddown = winddown(end_time.time())
    total_days = start_time_winddown + 1 - end_time_winddown + trading_days - 1
    return total_days / 252



def bs_implied_vol(F,K,t,kind,price):
    r = 0
    try:
        iv = implied_volatility(price, F,K,t,r, kind.lower())
    except:
        iv = 0
    return iv

def bs_delta(F,K,t,kind,iv):
    r = 0
    try:
        bs_delta = delta(kind.lower(), F,K,t,r, iv)
    except:
        bs_delta = 0
    return bs_delta