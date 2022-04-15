def calc_price_final(gross_price, calc_impost, *params):
    return gross_price + gross_price * calc_impost(*params)


def impost_x(imported):
    return 0.22 if imported else 0.13


def impost_y(explosive, multi_fact=1):
    return 0.11 * multi_fact if explosive else 0


if __name__ == '__main__':
    gross_price = 100.00
    final_price = calc_price_final(gross_price, impost_x, True)
    final_price = calc_price_final(final_price, impost_y, True, 1.5)
    print(f'The final price is {final_price}')
