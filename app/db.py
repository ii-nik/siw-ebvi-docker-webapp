import os
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
dbhost = os.environ["DB.HOST"]
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'siwusers'
app.config['MYSQL_DATABASE_HOST'] = dbhost
mysql.init_app(app)
