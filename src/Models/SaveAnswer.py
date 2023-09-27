class SaveAnswers:
    def __init__(self,conn,cursor):
        self.conn = conn 
        self.cursor = cursor
        self.table = "save_answers"
    
    def save_question(self, aid, uid):
        sql = f"INSERT INTO {self.table}(a_id, user_id) VALUES(%s,%s)"
        try:
            self.cursor.execute(sql, (aid,uid))
            self.conn.commit()
	except:
	    return False
   
    def delete_saved_question(self,qid):
        sql = f"DELETE FROM {self.table} WHERE sa_aid= %s"
        self.cursor.execute(sql,(qid,))
