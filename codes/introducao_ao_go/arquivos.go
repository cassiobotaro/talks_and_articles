package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	d1 := []byte("hello go\n")
	err := ioutil.WriteFile("/tmp/dat", d1, 0644)
	if err != nil {
		log.Fatal(err)
	}

	dat, err := ioutil.ReadFile("/tmp/dat")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(string(dat))

}
