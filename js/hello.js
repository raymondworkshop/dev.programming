"use strict";

var message = "Hello World";
console.log(message)

function ask(question, yes, no) {
    if (question) yes()
    else no();
}

ask(
    "Do you agree?",
    function () { console.log("You agree."); },
    function () { console.log("YOu canceled the execution."); }
)