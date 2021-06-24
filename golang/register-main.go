package main

import (
	"fmt"
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	// Imagine you have a worker pool and want to count the tasks completed.
	taskCounter := prometheus.NewCounter(prometheus.CounterOpts{
		Subsystem: "worker_pool",
		Name:      "completed_tasks_total",
		Help:      "Total number of tasks completed.",
	})
	// This will register fine.
	if err := prometheus.Register(taskCounter); err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("taskCounter registered.")
	}

	
	// Don't forget to tell the HTTP server about the Prometheus handler.
	// (In a real program, you still need to start the HTTP server...)
	http.Handle("/metrics", promhttp.Handler())

	// Now you can start workers and give every one of them a pointer to
	// taskCounter and let it increment it whenever it completes a task.
	taskCounter.Inc() // This has to happen somewhere in the worker code.

	http.ListenAndServe(":8080", nil)
	//taskCounterVec.WithLabelValues("42").Inc() // Code from worker 42.

	// Each worker could also keep a reference to their own counter element
	// around. Pick the counter at initialization time of the worker.
	//myCounter := taskCounterVec.WithLabelValues("42") // From worker 42 initialization code.
	//myCounter.Inc()                                   // Somewhere in the code of that worker.
}