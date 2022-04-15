from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, description, **kwargs):
        self.tasks.append(Task(description, kwargs.get('Due Date', None)))

    def add(self, task, due_date=None, **kwargs):
        chosen_function = self._add_task if isinstance(task, Task) \
            else self._add_new_task
        kwargs['Due Date'] = due_date
        chosen_function(task, **kwargs)

    def outstanding(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        # IndexError ??
        return [task for task in self.tasks
                if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.outstanding())}) task(s) outstanding!'


class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.due_date = due_date

    def complete(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Done)')
        elif self.due_date:
            if datetime.now() >= self.due_date:
                status.append('(Overdue)')
            else:
                Days = (self.due_date - datetime.now()).days
                status.append(f'-> Expire in {Days} days!')
        return f'{self.description} ' + ' '.join(status)


class RecurrentTask(Task):
    def __init__(self, description, due_date, Days=7):
        super().__init__(description, due_date)
        self.Days = Days

    def complete(self):
        super().complete()
        new_due_date = datetime.now() + timedelta(days=self.Days)
        return RecurrentTask(self.description, new_due_date, self.Days)


def main():
    Home = Project('HomeWork')
    Home.add('Iron clothes', datetime.now())
    Home.add('Wash the dishes')
    Home.add(RecurrentTask('Change the sheets', datetime.now(), 7))
    Home.add(Home.search('Change the sheets').complete())
    print(Home)

    Home.search('Wash the dishes').complete()
    for task in Home:
        print(f'- {task}')
    print(Home)

    # Espaço para orgazinar o output
    print('        ')
    print('        ')

    Market = Project('Shopping in the Market')
    Market.add('Fruits', datetime.now() + timedelta(days=3))
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
