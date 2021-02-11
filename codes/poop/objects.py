#!.venv/bin/python3

# envia uma mensagem ao objeto 1 para invocar o método bit_length
(1).bit_length()

# outro jeito de fazer a mesma coisa
getattr(1, "bit_length")()

# invoca a função embutida str no objeto 1, retornando um objeto string
str(1)

# podemos invocar a função dunder str, é equivalente, mas não é recomendada
(1).__str__()

# envia uma mensagem ao objeto que invoca um método
getattr(1, "__str__")()

# podemos acessar o "molde" utilizado para construir o objeto
(1).__class__

# o que mais abstraimos em classes?
