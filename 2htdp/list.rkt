#lang racket
;
(require 2htdp/batch-io)
; TODO - 10.3 Lists in Lists, Files
;
;  Data representation  
;
;   A list of string (los) is -
;    - '()
;    - (cons String los)
(cons "TTT" '())
(cons "" (cons "TTT" '()))
(cons "Put up in a place" (cons "" (cons "TTT" '())))
(read-file "ttt.txt")
; 
;  A list of words (low) is -
;    - '()
;    - (cons String lows)
(cons "TTT" '())
(cons "Put" (cons "TTT" '()))
(read-words "ttt.txt")
;
;  A list of list of strings (lls) is - 
;    - '() 
;    - (cons String lls) 
(cons "TTT" '())
(cons "" (cons "TTT" '()))
(cons "Put" (cons "" (cons "TTT" '())))
(cons "up" (cons "Put" (cons "" (cons "TTT" '()))))
(read-words/line "ttt.txt")
;
;
; how many words appear per line 
; 
; list of lists of strings (lls) -> list-of-numbers  
; determines the number of words on each line 
; data examples
(define line0 '())
;(define line1 (cons "world" '()))
(define line2 (cons "hello" (cons "world" '())))

(define lls0 '())
;(define lls1 )

;  the head of desired function
(define (words-on-line lls) '())
