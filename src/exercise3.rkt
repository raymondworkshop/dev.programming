#lang racket
(require racket/trace)

(require "str.rkt")

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


;; Pig Latin
(define (pigl wd)
  (if (pl-done? wd)
      (word wd "ay")
      (pigl (word (ch-bf wd) (ch-first wd)))))

(define (pl-done? wd)
  (vowel? (ch-first wd)))

(define (vowel? letter)
  (member? letter '("a" "e" "i" "o" "u")))

; Count-ums
(define (count-ums-v1 lst)
  (cond ((empty? lst) 0)
        ((first-ums? lst) (+ 1 (count-ums  (rest lst))));
        (else (count-ums (rest lst)))))

(define (count-ums lst)
  (if (empty? lst)
      0
      (if (first-ums? lst) ; the first word of the list is "um"
          (+ 1 (count-ums (rest lst)))
          (count-ums (rest lst)))
      ))

(define (first-ums? lst)
  (equal?  (first lst) "um"))
