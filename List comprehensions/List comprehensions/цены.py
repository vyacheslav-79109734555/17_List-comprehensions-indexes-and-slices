def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_list = [1.09, 23.56, 57.84, 4.56, 6.78]

x = int(input('Повышение стоимости товара на первый год в %: '))
y = int(input('Повышение стоимости товара на второй год в %: '))

prices_x = [get_higher_price(x, i_price) for i_price in prices_list]
prices_y = [get_higher_price(y, i_price) for i_price in prices_x]

print('Сумма цен за каждый год:', round(sum(prices_list), 2), round(sum(prices_x), 2), round(sum(prices_y), 2))
