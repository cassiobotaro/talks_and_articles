@dataclass
class User:
    '__init__, __repr__, __eq__ are generated automatically'
    name: str
    age: int
    active: bool = False

user1 = User(name='cassio', age=27)
user1.active = True

user2 = User(name='joe', age=21)

print('same user? ', user1 == user2)
