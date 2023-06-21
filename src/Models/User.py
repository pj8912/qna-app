class User:
    def __init__(self, cursor, cnx):
        self.table = "users"
        self.cursor = cursor
        self.cnx = cnx

    def create_user(self, flname,uname,pwd):
        sql = f"INSERT INTO users(fullname, user_uname, user_pwd) VALUES(%s,%s,%s)"
        self.cursor.execute(sql, (flname,uname,pwd))
        self.cnx.commit()

    def get_user_by_username(self,uname):
        sql = f"SELECT * FROM {self.table} where user_uname=%s"
        self.cursor.execute(sql,uname)
        result = self.cursor.fetchone()
        return result


    
