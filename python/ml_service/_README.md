#### The Project
* A python app ml_service that can be used use to train a model that predicts the variable
score based on the given variables age and species by sending JSON data to it over HTTP.

* The required pkg is in the requirements.txt

* Flask Framework is used here

#### words

I spend about 7 hours for the project. 
The main reasons are:
  * I didn't use Flsk framework firstly, and tried to write some functions to convert curl to python code 
  * Some problems/Debug on Database
  * Check some doc on SQLite3 and sklearn


#### Run
>Start the server
$  python ml_service.py &

>send a training examples
$  curl -H "Content-Type: application/json" \
-X POST -d '{"age": 1.1, "species": "cat", "score": 3.1}' \
http://127.0.0.1:5000/learn

ok

>Train model
$  curl -X POST http://127.0.0.1:5000/train
ok

>prediction
$ curl -H "Content-Type: application/json" \
-X POST -d '{"age": 4.5, "species": "dog"}' \
http://127.0.0.1:5000/predict

{"score": 3.1}



#### Database schema

* db_model.py define the schema

* SQLite3 Database is used here


#### ML Model

* liner Regression model is used in 


#### The running log
$$$$(proj-Z5UivSYb) zhaowenlong@zhaowenlongs-MacBook:~/workspace/proj/dev.programminglanguage/python/ml_service$ curl -H "Content-Type: application/json" -X POST -d '{"age": 1.1, "species": "cat", "score": 3.1}' http://127.0.0.1:5000/learn
Sending data ...
The entry: [1.1@cat@3.1]
127.0.0.1 - - [25/Jan/2018 23:01:23] "POST /learn HTTP/1.1" 200 -
ok


$$$$(proj-Z5UivSYb) zhaowenlong@zhaowenlongs-MacBook:~/workspace/proj/dev.programminglanguage/python/ml_service$ curl -X POST http://127.0.0.1:5000/train
Training the model ...

/Users/zhaowenlong/.virtualenvs/proj-Z5UivSYb/lib/python3.6/site-packages/scipy/linalg/basic.py:1226: RuntimeWarning: internal gelsd driver lwork query error, required iwork dimension not returned. This is likely the result of LAPACK bug 0038, fixed in LAPACK 3.2.2 (released July 21, 2010). Falling back to 'gelss' driver.
  warnings.warn(mesg, RuntimeWarning)
127.0.0.1 - - [25/Jan/2018 23:04:51] "POST /train HTTP/1.1" 200 -
ok

$$$$(proj-Z5UivSYb) zhaowenlong@zhaowenlongs-MacBook:~/workspace/proj/dev.programminglanguage/python/ml_service$  curl -H "Content-Type: application/json" \
-X POST -d '{"age": 4.5, "species": "dog"}' \
http://127.0.0.1:5000/predict

{"score": 3.1}


#### Q&A
