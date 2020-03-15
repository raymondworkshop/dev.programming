
#### notes  

##### ch4 - Data Processing  
* lazy computation - computing values **on demand** instead of being retrieved from an existing memory source  

  -   



##### ch1 - Building Abstractions with Functions  

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

  - higher-order functions 
    + how **functions can be manipulated as data** using higher-order functions  
  - 

#### ch2 - Building Abstractions with Data  
  - struct programs on abstract data  
  - data abstraction manipulate **compound values as units**  
    + isolate **how data are represented (as parts)** and **how data are manipulated (as units)**  

  - Data  
    + how data can be endowed with behavior using message passing and an object system  

#### Organize large programs  
  - **build modular, maintainable, and extensible programs**       
  - functional abstraction  
    + **a method of abstraction that describe compound operations** independent of a particular values  

  - data abstraction  - abstraction barrier  
    +  we can express abstract data using **a collection of selectors and constructors, together with some behavior**  


    + As long as **the behavior conditions are met** (such as the division property),** the selector and constructors constitute a valid representation** of a kind of data  
    + 

    + identify a basic set of operations, and then to use only those operations in manipulating the data
    + by restricting the use of operations, it is easier to change the representation of abstract data without chaning the behavior of a program  
    + 
    +  like in [this](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/data_abstraction.py),  function numer() and denom() as selectors, and function rational() as constructors to construct the function add_rational(), mul_rational()  
    + 
  - class inheritance  
    + like [this](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/oop.py)
  
  - generic function  
    + like [this](https://github.com/muyun/dev.programming/blob/master/python/exercise_py/generic_function.py)  
    + like [this]()



#### reference
