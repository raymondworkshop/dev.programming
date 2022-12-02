
#### programming  
* programmers combine primitive elements to form compound objects, they abstract compound objects to form higher-level building blocks, and they preserve modularity by adopting appropriate large-scale views of system structure.  
    - primitives -> compound objects -> higher-level blocks -> module -> system  

* Metalinguistic abstraction — establishing new languages  
    - Establishing new languages is a powerful strategy for controlling complexity in engineering design  
    - enhance our ability to deal with a complex problem by adopting a new language that enables us to **describe (and hence to think about) the problem in a different way**, using primitives, means of combination, and means of abstraction that are particularly well suited to the problem at hand

#### Python  
* Python provides **a kind of "domain language" for thinking about your problem**    
    - **Python Data Model**, and its API to make our own objects  
        + **The built-in operators and expressions are at the core** of that language and everything else builds from it.  

        + we leverage the Python Data Model to build new classes  
            - implement special methods when we want out objects to support and interact with fundamental language constructs  
            - the Python interpreter **invokes special methods to perform** basic object operations  
  
    - one you build **a kind of intuition around python's built-in objects and operations**, you will find that your intuition applies everywhere  
        
* Object, and Protocols  
    - everything in Python is first-class  
    - **All objects can be treated as data**    


#### tips  
* ipdb debugger  
    >  import ipdb; ipdb.set_trace()  
    >  
    >  python -m ipdb X.py

* env  
    > python3 -m venv programenv  
    > source  programenv/bin/activate   
    > deactivate  

* common commands on vim  
    - :sp (:split) -> split vim the window horizontally  
    - :vsp (:vsplit) -> split vim window vertically  
    - Ctrl + wj -> move cursor to the window below (horizontal split)  
    - Ctrl + wk -> move cursor to the window below (horizontal split)  
    - Ctrl + wh -> move cursor to the left window (vertical split)
    - Ctrl + wl -> move cursor to the right window (vertical split)



#### reference  
* **[Composing Programs](https://composingprograms.com/)**
* **[SICP-2nd](http://sarabander.github.io/sicp/html/index.xhtml#SEC_Contents)**  
* [SICP-JS](https://sourceacademy.org/sicpjs/acknowledgements)  
* [SICP-guile](https://github.com/zv/SICP-guile)  
* **[how to design programs-2nd](https://htdp.org/2018-01-06/Book/index.html)**  
* **[The Art of Unix Programming](http://www.catb.org/~esr/writings/taoup/html/)** 
* [The Practice of Programming](https://book.douban.com/subject/1459281/)
* [Eloquent JavaScript](https://eloquentjavascript.net/)
* [软件随想录 - 关于战略问题的通信之六]  
* [vim](https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)
