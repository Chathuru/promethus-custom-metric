package main

import (
        "net/http"      
        "github.com/prometheus/client_golang/prometheus"
        "github.com/prometheus/client_golang/prometheus/promhttp"
        "math/rand"
)      

var (
        gauge = prometheus.NewGauge(
                        prometheus.GaugeOpts{
                        //Namespace: "golang",
                        Name:      "my_gauge",
                        Help:      "This is my gauge",
                })
)

func metrics(w http.ResponseWriter, r *http.Request) {
        //registry := prometheus.NewPedanticRegistry()
        registry := prometheus.NewRegistry()
        registry.MustRegister(gauge)

        gauge.Add(rand.Float64()*15 - 5)

        h := promhttp.HandlerFor(registry, promhttp.HandlerOpts{})
	h.ServeHTTP(w, r)
}

func main() {
        http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte(`<html>
			<head><title>Node Exporter</title></head>
			<body>
			<h1>Node Exporter</h1>
			<p><a href="/metrics">Metrics</a></p>
			</body>
			</html>`))
	})

        http.HandleFunc("/metrics", metrics)
        http.ListenAndServe(":8080", nil)
}
