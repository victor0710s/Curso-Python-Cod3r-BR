class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.actual_speed = 0

    def speedup(self, delta=5):
        max = self.max_speed
        new = self.actual_speed + delta
        self.actual_speed = new if new <= max else max
        return self.actual_speed

    def speeddown(self, delta=5):
        new = self.actual_speed - delta
        self.actual_speed = new if new >= 0 else 0
        return self.actual_speed


if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        print(c1.speedup(8))

    for _ in range(10):
        print(c1.speeddown(delta=20))
