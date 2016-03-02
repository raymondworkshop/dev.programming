#lang racket

; word procedure takes any number of words into one big word
(define word string-append)


; sentence or se procedure takes in a list of string and creates one sentence
(define (se lst)
  (if (empty? (rest lst)) (first lst)
      (word (first lst) " " (se (rest lst)))))

(define sentence se)

; define procedure member?
(define (member? x lst)
  (if (null? lst)
      #f
      (if (equal? x (first lst))
          #t
          (member? x (rest lst)))))
