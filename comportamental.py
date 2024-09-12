# observer.py

from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserverA(Observer):
    def update(self, state):
        print(f"ConcreteObserverA: Reacted to the event. New state: {state}")

class ConcreteObserverB(Observer):
    def update(self, state):
        print(f"ConcreteObserverB: Reacted to the event. New state: {state}")

# Uso do padrão
if __name__ == "__main__":
    subject = Subject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.set_state("Estado 1")
    subject.set_state("Estado 2")

    subject.detach(observer_a)

    subject.set_state("Estado 3")