package main

import "fmt"

type Identificador int

type Aluno struct {
	nome  string
	idade int
	id    Identificador
}

func newAluno(nome string, idade int) *Aluno {
	return &Aluno{nome: nome, idade: idade, id: 42}
}

func (aluno Aluno) VerificaAluno(id Identificador) bool {
	return id == aluno.id
}

func main() {
	aluno := newAluno("Cássio", 23)
	fmt.Println(aluno.VerificaAluno(10))
}
