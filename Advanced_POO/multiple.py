# Herança Multipla

class Animal:
    @property
    def capacity(self):
        return ('sleep', 'eat', 'drink')


class Man(Animal):
    @property
    def capacity(self):
        return super().capacity + ('love', 'speak', 'study')


class Spider(Animal):
    @property
    def capacity(self):
        return super().capacity + ('make web', 'walk through the walls')


class SpiderMan(Spider, Man):
    @property
    def capacity(self):
        return super().capacity + \
            ('beat up thugs', 'shoot web between buildings')


if __name__ == '__main__':
    John = Man()
    print(f'John: {John.capacity}')

    spider = Spider()
    print(f'spider: {spider.capacity}')

    Peter = SpiderMan()
    print(f'Peter: {Peter.capacity}')
