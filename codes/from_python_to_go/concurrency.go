package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	urls := []string{
		"https://httpbin.org/delay/2",
		"https://nuveo.com.br",
		"https://google.com",
		"https://httpbin.org/status/200",
		"https://httpbin.org/status/201",
	}
	// ...
	for _, url := range urls {
		wg.Add(1)
		go func(url string) { // HL
			defer wg.Done()           // HL
			res, err := http.Get(url) // HL
			if err != nil {           // HL
				log.Fatal(err) // HL
			} // HL
			fmt.Println(url, "->", res.StatusCode) // HL

		}(url) // HL
	}
	wg.Wait()
}
