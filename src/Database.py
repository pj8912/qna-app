import mysql.connector
from dotenv import load_dotenv
load_dotenv()
class Database:
  def __init__(self):
    self.HOST = os.environ.get("DB_HOST")
    self.USERNAME = os.environ.get("DB_USERNAME")
    self.PWD = os.environ.get("DB_PWD")  
    self.DBNAME = os.environ.get("DB_NAME")

    #create connection
    self.cnx = mysql.connector.connect(user=USERNAME,password=PWD,host=HOST, database=DBNAME)
    self.cursor = cnx.cursor()
    
