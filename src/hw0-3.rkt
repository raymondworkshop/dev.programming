#lang racket
(require racket/trace)

; defining procedures, the procedure body is not evaluated when it is defined
; factorial
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

;
(define (fib n)
  (cond
    [(= n 0) 0]
    [(= n 1) 1]
    (else (+ (fib (- n 1))
             (fib (- n 2))))))
