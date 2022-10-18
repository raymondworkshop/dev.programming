
#### Project  
* plan  
    - **think about the specifications** of the program 
    you're planning to build  

    - make writing the programs a more **intuitive** task  


#### namespace  
* start with a package  -> all of code remains isolated  
    - put starting code in __main__.py and run it using python -m program  
    ```
    program/
        __init__.py  
        __main__.py  
    ```  

    - use package-relative imports  

* package  
    - a package is a collection of modules that are **grouped under a common top-level name**    
    - __init__.py file is to **build and/or manage the contents of the top-level package namespace**   

* modules  
    - modules as abstraction layers to **separate code into parts**  
    - python interpreter search for models **in the "path"** recursively 
        + the included code is isolated in **a module namespace**, and neednot worry the included codde have unwanted effects  

    - group modules together in a package  


* pure functions  
    - more efficient building blocks than classes and objects 
    with **no context or side-effects** 
    - easier to test with unit tests    
   
* class 



#### Python Data Model - A Framework/API for core language constructs

Python interpreter invokes special methods to perform basic object operations.

By using and implementing special methods of Python Data Model in your objects, your objects can **behave like the built-in types**, enabling the expressive coding style **Pythonic**.

#### Data Sturctures
* sequences - Python sequences are often categorized as **mutalbe or immutable**, and also could be considered as **flat sequences and container sequences**.
    + container sequences -> hold **references** to the objects
    + flat sequences (like str, bytes) -> more compact because of the physically store the value
    
    + **list** -> mutable and mixed-type
        - list comprehensions and generator expression

    + **tuples** -> immutable lists
        - tuples can hold records
        - tuple unpacking -> parallel assignment

    + array -> efficient because of only **the packed bytes for numeric data**
        - for large sequences of numbers, this saves a lot of memory
        - NumPy lib
  
* collections  
    + dict and set  
        - **hash tables** are the engines for the high performance dicts
        - hash tables must be sparse to work, they are **not space efficient**, compared to a low-level array a pointers to its elements (more compact but also much lower to search)  

    + Data class as a collection of fields  
  
* str versus bytes  

* Variables are mere labels  
    - the parameters in the function are **aliases** of the actual arguments  

#### Functions as objects  

* Functions, like integers, strings, and dictionaries, also can be a **program entity**, this enables programming in a **functional style**. 
    + The main ideas are that we can assign functions to variables, pass them to other functions, store them in data structures and access function attributes.
    
* function decorators and closures
  
    
#### Object Oriented

#### Control flow  
* Generators - declare a function that behaves like an iterator 
    + yield -> return the generator object 
        - yield pauses the function and saves the local state so that it can be resumed right where it left off 

* Concurrency 


#### Metaprogramming 


#### reference  
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/#)
* [Rewriting Reddit](http://www.aaronsw.com/weblog/rewritingreddit)

* [Python Stacks, Queues, and Priority Queues in Practice](https://realpython.com/queue-in-python/#integrating-python-with-distributed-message-queues)
* [The Python Language Reference](https://docs.python.org/3/reference/lexical_analysis.html)
* [A Conversation with Guido van Rossum](https://www.artima.com/intv/guido.html) 
* [_why's Estate](https://viewsourcecode.org/why/)  
* [Chapter 14- Languages](http://www.catb.org/~esr/writings/taoup/html/ch14s04.html#c_lang)
* [Fluent Python - 2nd](https://learning-oreilly-com.easyaccess1.lib.cuhk.edu.hk/library/view/fluent-python-2nd/9781492056348/ch01.html#collection_api)
* [Learn by reading code](https://death.andgravity.com/stdlib)
* [Effective Python 2rd](https://learning-oreilly-com.easyaccess2.lib.cuhk.edu.hk/library/view/effective-python-90/9780134854717/?ar) 
* [How to Think Like a Computer Scientist](http://interactivepython.org/runestone/static/thinkcspy/toc.html)
* [4.1. Abstract Data Types](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/ADT.html)