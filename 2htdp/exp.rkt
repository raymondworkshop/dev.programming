#lang racket

(string-append "Hello World")

(cos pi)

(require 2htdp/image (only-in pict show-pict))
;(require racket/gui/base)

(show-pict (circle 10 "solid" "red"))