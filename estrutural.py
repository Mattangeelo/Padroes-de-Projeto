# adapter.py

class Target:
    def request(self):
        return "Target: O comportamento padrão do alvo."

class Adaptee:
    def specific_request(self):
        return ".eetpadA od ocifícepse otnematropmoC"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRADUZIDO) {self.adaptee.specific_request()[::-1]}"

# Uso do padrão
def client_code(target):
    print(target.request())

if __name__ == "__main__":
    print("Cliente: Posso trabalhar perfeitamente com objetos Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: A classe Adaptee tem uma interface estranha. "
          "Veja, eu não entendo:")
    print(f"Adaptee: {adaptee.specific_request()}")
    print("\n")

    print("Cliente: Mas posso trabalhar com ela através do Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)