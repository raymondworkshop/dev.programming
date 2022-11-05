
#### About [Composing Programs](http://composingprograms.com/pages/11-getting-started.html)    
* how computers interpret computer programs and carry out computational processes  
* some recent progress in computer programs  



#### ch2 - Data Abstraction - Building Abstractions by combining data objects to form compound data    

- how data can be endowed **with behavior using message passing and an object system**    

- **data abstraction**  manipulate compound values as units
    + how compound data is used    
    + how compound data are represented    
        - **the interface/barriers** between these two parts of system will be a set of functions, called **selectors and constructors**  
        - like in [data_abstraction.py](https://github.com/muyun/dev.programming/blob/master/sicp/python/data_abstraction.py),  function numer() and denom() as selectors, and function rational() as constructors to construct the function add_rational(), mul_rational()  


- **Sequence paradigm** (implemented as lists) as conventional interface    
    + The representation of sequences in terms of **lists** or **trees**   
        - like [tree.py](https://github.com/muyun/dev.programming/blob/master/sicp/python/tree.py) or [link.py](https://github.com/muyun/dev.programming/blob/master/sicp/python/link.py)   
    
    + **express programs as sequence operations**,and **make program designs that are modular**      
        - **modular design by providing a library of components together** with a conventional interface for connecting the components in flexible ways  
            + filter, map, accumulate  

    + **chaining together a pipeline of functions**, if the functions all take a sequence as an input and output  
        - like [sequences.py](https://github.com/muyun/dev.programming/blob/master/sicp/python/sequences.py)  
    

- Mutable Data allows us to simulate systems with change  
    + Add state to data  
        - data can have behavior  
        - Functions could be manipulated as data  

    + nonlocal assignment  
        - only function calls can introduce new frames  

        - Using nonlocal, we can view a program as a collection of independent and autonomous objects  (interact with each other but each manage their own internal state)
            + **Different parts of a program**, which **correspond to different environment frames**, can evolve separately throughout program execution  -> modular 
            + **using functions with local state**, we can implement abstract data types  
                -  **A mutable linked list is a function**, the example [mutable_data.py](https://github.com/muyun/dev.programming/blob/master/sicp/python/mutable_data.py), a mutable list is implemented, and the message passing fucntion is used  


- **class inheritance**       
    + TODO 2.5  
    + like [oop.py](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/oop.py)  
  
- **generic functions**      
    + like [generic_function.py](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/generic_function.py)   
    + generic functions are methods or functions that apply to argumetns of diff types  
        - [generic_function_1.py](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/generic_function_1.py)      



##### ch1 - Building Abstractions with Functions  
* how functions can be manipulated **as data using higher-order functions**  

* **functional abstraction**    

* represent **procedures (descriptions of processes) as data**  
    - Lisp’s flexibility in handling procedures as data 
    -  blur the traditional distinction between “passive” data and “active” processes.


* The programming language serves a **framework where we organize our ideas** about computational processes   
    - combine simple ideas to form more complex ideas  
        + primitive expressions and statements  
        + **combination** -> compound elements are built from simpler ones  
        + **abstraction** -> compound elements can be named and manipulated as units  
    - **combine and abstract** both data and functions  
    - pure function 
        + has no effects beyond returning a value  
        + return the same value when called twice with the same args  
    - Testing  
        + assert 

    - **control abstraction** using recursion, higher-order functions, generators, and streams  
        + higher-order functions 
            - how **functions can be manipulated as data** using higher-order functions  


##### ch4 - Data Processing  
* lazy computation - computing values **on demand** instead of being retrieved from an existing memory source  
    -  TODO - Implement stream class 


#### ch3 - **language abstraction** using interpreters and macros  


#### reference  
* **[Composing Programs](https://composingprograms.com/)**  
* **[how to design programs-2nd](https://htdp.org/2018-01-06/Book/index.html)**  
* **[CS 61A: Structure and Interpretation of Computer Programs](https://cs61a.org/)** 
* [Essentials of Programming Languages](https://book.douban.com/subject/3136252/)  
* [Racket Scheme & SICP](https://news.ycombinator.com/item?id=25442005)
* [SICP in JS](https://sourceacademy.org/sicpjs/index)
* [SICP in python](https://wizardforcel.gitbooks.io/sicp-in-python/content/8.html)  
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/#)
* [History of Tcl](http://www.tcl.tk/about/history.html)
* [SICP-guile](https://github.com/zv/SICP-guile)  
* [A Scheme Primer](https://spritely.institute/static/papers/scheme-primer.html)
* [how to design programs-2nd](https://htdp.org/2018-01-06/Book/index.html) 
* the little scheme  

* [Why Study Functional Programming?](https://acm.wustl.edu/functional/)