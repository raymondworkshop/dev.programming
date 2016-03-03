#lang racket
;http://www.cs61as.org/textbook/homework-0.2.html
(require racket/trace)

(require "str.rkt")
;(provide (all-defined-out))
;

; ex1
; the first two ch of the wd
(define (first-two wd)
  (word (word-first wd) (word-first (word-bf wd))))

;
(define (two-first wd1 wd2)
  (word (word-first wd1) (word-first wd2)))

(define (two-first-sent lst)
  (word (word-first (first lst)) (word-first (first (rest lst)))))

;ex2
(define (teen? num)
  (and (>= num 13) (<= num 19))
  (error "Not yet implemented"))


;ex3
(define (indef-article wd)
  (if (vowel-start? wd)
      (word "an" " "  wd)
      (word "a" " " wd)))

(define (vowel-start? wd)
  (member? (word-first wd) (list "a" "o" "e" "i" "u")))

;ex4
(define (insert-and lst)
  (se lst))

; ex5
(define (query lst)
  (se (list (first (rest lst))  (first lst)  (se (rest (rest lst))) "?") ))

;ex6 
(define (european-time tm notation)
  (cond
    ((equal? notation 'am) (if (= tm 12)
                               0
                               tm))
    ((equal? notation 'pm) (+ tm 12)) ))

(define (american-time tm)
  (if (>= tm 12)
      (se (list (number->string (- tm 12)) "pm"))
      (se (list (number->string tm) "am"))))

; ex7
