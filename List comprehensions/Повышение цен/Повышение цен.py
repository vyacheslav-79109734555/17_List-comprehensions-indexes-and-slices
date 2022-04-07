def rise_in_price(percent, i_a_b_list):
    return i_a_b_list * (1 + percent / 100)


a_list = [1.09, 23.56, 57.84, 4.56, 6.78]

for i in a_list:
    print('Цена на товар:', i)

x = int(input('Повышение стоимости товара на первый год в %: '))  # percent
y = int(input('Повышение стоимости товара на второй год в %: '))  # percent

b_list = [rise_in_price(x, i_a_list) for i_a_list in a_list]
c_list = [rise_in_price(y, i_b_list) for i_b_list in b_list]

print('Сумма цен за каждый год: ', round(sum(a_list), 2), round(sum(b_list), 2), round(sum(c_list), 2))
