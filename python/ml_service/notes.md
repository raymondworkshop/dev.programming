#### about database
from ml_service import db
db.create_all()
from app import Data
db1 = Data(age=4.5, species='dog', score=3.1)
db2 = Data(age=6.5, species='cat', score=4.1)
db.session.add(db1)
>>> db.session.add(db2)
>>> db.session.commit()

#### reference
* [Implementing a RESTful Web API](http://blog.luisrei.com/articles/flaskrest.html)