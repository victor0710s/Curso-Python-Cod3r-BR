from datetime import datetime


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
    Home = []
    Home.append(Task('Iron the clothes'))
    Home.append(Task('Wash the dishes'))

    [task.complete() for task in Home if task.description == 'Wash the dishes']

    for task in Home:
        print(f'- {task}')


if __name__ == '__main__':
    main()
