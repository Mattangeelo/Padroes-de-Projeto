# factory_method.py

from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: O mesmo código do criador acabou de trabalhar com {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "Resultado do ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self):
        return "Resultado do ConcreteProduct2"

# Uso do padrão
def client_code(creator: Creator):
    print(f"Client: Não conheço a classe do criador, mas ainda funciona.\n"
          f"{creator.some_operation()}")

if __name__ == "__main__":
    print("App: Lançado com ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Lançado com ConcreteCreator2.")
    client_code(ConcreteCreator2())