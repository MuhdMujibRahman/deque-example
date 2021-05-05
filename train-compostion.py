from collections import deque
from collections import deque
class TrainComposition:

    def __init__(self):
        self.wagons = deque()

    def attach_wagon_from_left(self, wagonId):
        self.wagons.insert(0,wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.wagons.append(wagonId)

    def detach_wagon_from_left(self):
        return self.wagons.popleft() if self.wagons else None

    def detach_wagon_from_right(self):
        return self.wagons.pop() if self.wagons else None


if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)

    print(train.detach_wagon_from_right())  # should print 7
    print(train.detach_wagon_from_left())  # should print 13
