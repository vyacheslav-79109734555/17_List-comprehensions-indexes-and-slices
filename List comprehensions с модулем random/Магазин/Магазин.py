original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [0 if i_prices <= 0 else i_prices for i_prices in original_prices]
print(new_prices)

