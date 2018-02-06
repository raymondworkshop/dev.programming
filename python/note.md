### Python
#### Python Data Model - A Framework/API for core language constructs

Python interpreter invokes special methods to perform basic object operations.

By using and implementing special methods of Python Data Model in your objects, your objects can **behave like the built-in types**, enabling the expressive coding style **Pythonic**.

#### Data Sturctures
  * sequences
  Python sequences are often categorized as **mutalbe or immutable**, and also could be considered as **flat sequences and container sequences**. 
    - list -> mutable and mixed-type
    - array
  
  * mappings
  * sets
  * str versus bytes
  
#### Functions as objects

#### Object Oriented

#### Control flow


#### Metaprogramming 


#### Notes
 * Reload modules problem in Emacs Python Shell
   - use importlib to reload(models) 
   - or use ipython and  %autoreload

 * virtualenvs setup for python3 -> pipenv
   - New a project: >pipenv --python 3.6
   - Install all dependencies:  >pipenv install
   - Locate the virtualenv: >pipenv --venv
   - Use the shell: >pipenv shell
   - Uninstall everything:  >pipenv uninstall --all

 * <del>Your environment contains PYTHONPATH=/usr/local/lib/python2.7/site-packages
This doesn't work with Python 3 for obvious reasons. To remove it:
> unset PYTHONPATH </del>

  * 