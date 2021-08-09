package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	res, _ := ioutil.ReadAll(r.Body)
	defer r.Body.Close()
	fmt.Fprintf(w, "Echo: "+string(res)+"\n")
}

func jsonHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	d := map[string]int{"apple": 5, "lettuce": 7}
	json.NewEncoder(w).Encode(d)
}

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/api/", jsonHandler)
	fmt.Println("Servindo em http://127.0.0.1:8080")
	http.ListenAndServe(":8080", nil)
}
