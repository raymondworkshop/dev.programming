#lang racket
(require 2htdp/image)
(require (only-in pict show-pict))
(require test-engine/racket-tests)
;
; A Graphical Editor - online editor for plain text
; 
; 5.10 - A Graphical Editor 
;   Data definition 
;   example 1) 
(define-struct editor1 [pre post])
; An Editor is a structure: 
;  (make-editor String String) 
; Interpretation (make-editor s t) describes an editor
; whose visible text is (string-append s t) with the cursor displayed beween s and t 
;
;  example 2)
(define-struct editor2 [txt cur])
; An Editor is a structure:
; (make-editor String Number)
; interpretation (make-editor s n) describes an editor 
; whose text is s with the cursor displayed in s[n]
;
; 10.4 - A Graphical Editor, Revisited 
; example 3)
(define-struct editor3 [pre post])
; An Editor is a structure:
;   (make-editor Lo1S Lo1S) 
; An Lo1S is one of:
;   - '()
;   - (cons 1String Lo1S) 

(define good (cons "g" (cons "o" (cons "o" (cons "d" '())))))
(define lla (cons "l" (cons "l" (cons "a" '()))))
(define all (cons "a" (cons "l" (cons "l" '()))))
; data example
(make-editor3 lla good) ; all good

; Lo1S -> Lo1S 
; reverse the given list
; TODO - finish
(check-expect (rev lla) all)
(define (rev l) 
  (cond
    [(empty? l) '()]
    [else 
     ( (first l)
       (rest l) )]))


;-------------------------------------------------
; Editor -> Image
(define SCENE (rectangle 200 20 "outline" "black"))
(define HORIZ-ALIGN "left")
(define VERT-ALIGN "middle")
(define X-ADJUST -3)
(define Y-ADJUST -1)

(define (render ed)
  (overlay/align/offset
   HORIZ-ALIGN VERT-ALIGN
   (show-pict (draw-text ed))
   X-ADJUST Y-ADJUST
   SCENE))

; Editor -> Image
; draw the text with cursor
(define (draw-text ed)
  (beside/align
   "bottom"
   (text (editor1-pre ed) 16 "black")
   (rectangle 1 20 "solid" "red")
   (text (editor1-post ed) 16 "black")))

;(render (make-editor1 "he" ""))
;(render (make-editor1 "hello" "world"))
(render (make-editor1 "hello " "world"))