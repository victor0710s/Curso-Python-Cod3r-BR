from datetime import datetime
from Store import Client, Seller, Purchase


def main():
    Victor = Client('Victor Silva', 19)
    Zuclene = Seller('Zuclene Maria', 53, 2000)
    purchase1 = Purchase(Zuclene, datetime.now(), 512)
    purchase2 = Purchase(Zuclene, datetime(2019, 10, 7), 10000)
    Victor.register_purchase(purchase1)
    Victor.register_purchase(purchase2)

    print(f'Client: {Victor}', '(adult)' if Victor.is_Adult() else '')
    print(f'Seller: {Zuclene}')
    print(f'Total: {Victor.total_purchases()} \
          in {len(Victor.purchases)} purchases')
    print(f'{Victor.get_last_purchase_date()}')


if __name__ == '__main__':
    main()
