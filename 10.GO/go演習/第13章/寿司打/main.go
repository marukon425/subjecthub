package main

import (
	"html/template"
	"log"
	"net/http"
)

func main() {
	tmpl := template.Must(template.ParseFiles("game.tmpl"))
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if err := tmpl.Execute(w, nil); err != nil {
			log.Println(err)
		}
	})
	log.Println("寿司打サーバー起動: http://localhost:8081")
	log.Fatal(http.ListenAndServe(":8081", nil))
}
