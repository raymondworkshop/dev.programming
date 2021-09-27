#lang racket
;
; 11 Design by Composition
;  note: know when to design several functions,
;  and how to compose these functions into one program  
; 
;(require test-engine/racket-tests)
(cons 1 (cons 2 (cons 3 '())))
(list 1 2 3)
;
(cons (cons 1 (cons 2 '()))
      (cons (cons 2 '())
            '()))
(list (list 1 2) (list 2))
;
; 11.2 Composing Functions 
;  note: 1. design one function per task 
;           - formulate auxiliary function definitions 
;             for each dependency between quantities in the problem
;        2. **design one template** per data definition  
;           - formulate auxiliary function definitions 
;             when one data definition points to a second data definition  
;
;    maintain **a Wish List of function headers** to complete a program  