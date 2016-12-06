package main

// Composition over inheritance
import "fmt"

type Explorer struct{}

func (exp Explorer) Search() {
	fmt.Println("Searching...")
}

type DeepExplorer struct {
	Explorer
}

func (dexp DeepExplorer) Search() {
	fmt.Println("Go deep")
	dexp.Explorer.Search()
}

func main() {
	dexp := DeepExplorer{}
	dexp.Search()
}
