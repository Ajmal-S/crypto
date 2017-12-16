import json
import requests
import pprint
from decimal import Decimal


def get_crypto_details(currency):

    headers = {'Content-Type': 'application/json'}
    api_url = 'https://api.cryptonator.com/api/full/{0}-usd'.format(currency)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# pprint.pprint(get_crypto_details('xrp'))

def get_ratio_for(cry1, cry2):
    crypto_details1 = get_crypto_details(cry1)
    crypto_details2 = get_crypto_details(cry2)
    cry1_details = {market['market']:market['price'] for market in crypto_details1['ticker']['markets']}
    cry2_details = {market['market']:market['price'] for market in crypto_details2['ticker']['markets']}
    for market in cry1_details.keys() &  cry2_details.keys():
        print(cry1+': '+market+'-'+cry1_details[market]+' || '+cry2+': '+market+'-'+cry2_details[market]+' || ratio '+str(Decimal(cry1_details[market])/Decimal(cry2_details[market])))
    # return(Decimal(cry2_details['Kraken'])/Decimal(cry2_details['Bittrex']))

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# counter = 0
# l = []
# while counter<10:
#     try:
#         l.append(get_ratio_for)
# x = np.linspace(0, 10, 10)
# y = np.sin(x)

# fig, ax = plt.subplots()
# line, = ax.plot(x, y, color='k')

# def update(num, x, y, line):
#     line.set_data(x[:num], get_ratio_for('eth','xrp'))
#     line.axes.axis([0, 10, 0, 5])
#     return line,

# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
#                               interval=25, blit=True)
# ani.save('test.html')
# plt.show()
get_ratio_for('eth','xrp')

