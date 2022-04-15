from datetime import datetime


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description):
        self.tasks.append(Task(description))

    def outstanding(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        # IndexError ??
        return [task for task in self.tasks
                if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.outstanding())}) task(s) outstanding!'


class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()

    def complete(self):
        self.done = True

    def __str__(self):
        return self.description + ('(Done)' if self.done else '')


def main():
    Home = Project('HomeWork')
    Home.add('Iron clothes')
    Home.add('Wash the dishes')
    print(Home)

    Home.search('Wash the dishes').complete()
    for task in Home:
        print(f'- {task}')
    print(Home)

    Market = Project('Shopping in the Market')
    Market.add('Fruits')
    Market.add('Meat')
    Market.add('Rice')
    Market.add('Shampoo')
    print(Market)

    buy_meat = Market.search('Meat')
    buy_meat.complete()
    for task in Market:
        print(f'- {task}')
    print(Market)


if __name__ == '__main__':
    main()
