#lang racket
;
;; note: interactive programs  
;

(require 2htdp/image 
         2htdp/universe
         (only-in pict show-pict))

(define (number->square s)
  (square s "solid" "red"))

;(show-pict (number->square 20))

(show-pict (big-bang 100 [to-draw number->square]))