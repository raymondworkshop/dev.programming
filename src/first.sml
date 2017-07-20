(* Standard ML programming *)

(* expression:
  -> Syntax is how we write down this expression
  -> Semantics is what that sth means -
     - type-checking (before program runs) -> produces a type or fails
     - evaluation (as program runs)        ->  produces a value or exception or infinite-loop
 *)

(* variable binding *)
(* ctrl-c ctrl-s to run the program*)

val x = 34;

val y = 17;

(* REPL: Read-Eval-Print-Loop *)

(* ctrl-d finish sml process *)

(* Functions:
   A function is a value.
   Add pow to environment so later expressions can call it*)

(* works only if y >= 0 *)
fun pow(x : int, y : int) =
  if y = 0
  then 1
  else x * pow(x, y-1)

val fortytwo = pow(2, 2+2) + pow(4,2) + 2;


(* Pairs *)
(* int * bool -> bool * int *)
fun swap(pr : int*bool) =
  (#2 pr, #1 pr)

fun sum_list (xs : int list) = (* [3,5] *)
  if null xs
  then 0
  else hd xs + sum_list(tl xs)

(* saving recursive results in local bindings is essential *)
