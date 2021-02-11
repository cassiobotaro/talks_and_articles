#!.venv/bin/python3
class Dog:
    # variável de classe, compartilhada por todas as instâncias
    kind = 'canine'

    def __init__(self, name):
        # variável de instância única para cada instância
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')
print(d.name)
print(e.name)
print(d.kind)
print(e.kind)
