from app.utils.generator import new_name
from app.business import name_exists
from app.business.backend import add_name


def main():
    while True:
        name = new_name()
        if not name_exists(name):
            add_name(name)
            break

    print(f'Created new test name:"{name}"')


if __name__ == '__main__':
    main()
