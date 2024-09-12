# Padrões de Projeto: Exemplos e Explicações

Este repositório contém exemplos e explicações de três padrões de projeto: um comportamental, um criacional e um estrutural. Os padrões escolhidos são:

1. Comportamental: Observer
2. Criacional: Factory Method
3. Estrutural: Adapter

Cada padrão é demonstrado com um exemplo em Python, acompanhado por uma explicação detalhada e um diagrama UML.

## 1. Observer (Comportamental)

### Problema
O padrão Observer resolve o problema de notificar múltiplos objetos (observadores) sobre mudanças em um objeto (sujeito) sem criar um acoplamento forte entre eles.

### Solução
O padrão Observer define uma relação um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

### Diagrama UML
```
+------------+          +----------------+
|  Subject   |          |   Observer     |
+------------+          +----------------+
| observers  |<>------->| update()       |
+------------+          +----------------+
| attach()   |               ^
| detach()   |               |
| notify()   |          +-----------------+
+------------+          | ConcreteObserver|
      ^                 +-----------------+
      |                 | update()        |
+---------------+       +-----------------+
|ConcreteSubject|
+---------------+
| state         |
| getState()    |
| setState()    |
+---------------+
```

### Exemplo de Código
Veja o arquivo `observer.py` para um exemplo de implementação do padrão Observer em Python.

## 2. Factory Method (Criacional)

### Problema
O padrão Factory Method resolve o problema de criar objetos sem especificar explicitamente sua classe exata.

### Solução
O Factory Method define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Isso permite que uma classe adie a instanciação para subclasses.

### Diagrama UML
```
+-------------+         +------------------+
|   Creator   |         |     Product      |
+-------------+         +------------------+
| factoryMethod() |     | interface        |
+-------------+         +------------------+
      ^                          ^
      |                          |
+------------------+    +------------------+
| ConcreteCreator |    | ConcreteProduct  |
+------------------+    +------------------+
| factoryMethod() |    | implementation   |
+------------------+    +------------------+
```

### Exemplo de Código
Veja o arquivo `factory_method.py` para um exemplo de implementação do padrão Factory Method em Python.

## 3. Adapter (Estrutural)

### Problema
O padrão Adapter resolve o problema de incompatibilidade entre interfaces de diferentes classes.

### Solução
O Adapter permite que classes com interfaces incompatíveis trabalhem juntas, convertendo a interface de uma classe em outra interface que o cliente espera.

### Diagrama UML
```
+-------------+    +-------------+
|   Client    |    |   Target    |
+-------------+    +-------------+
                   | request()   |
                   +-------------+
                          ^
                          |
                   +--------------+
                   |   Adapter    |
                   +--------------+
                   | request()    |
                   +--------------+
                          |
                          |
                   +--------------+
                   |   Adaptee    |
                   +--------------+
                   | specificReq()|
                   +--------------+
```

### Exemplo de Código
Veja o arquivo `adapter.py` para um exemplo de implementação do padrão Adapter em Python.

## Como usar este repositório

1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Examine os arquivos Python para ver as implementações dos padrões.
4. Execute os arquivos Python para ver os padrões em ação.

Sinta-se à vontade para explorar, modificar e experimentar com os códigos!