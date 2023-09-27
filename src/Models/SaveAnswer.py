class SaveAnswers:
    def __init__(self,conn,cursor):
        self.conn = conn 
        self.cursor = cursor
        self.table = "save_answers"
    
    def save_question(self, qid, uid):
        sql = f"INSERT INTO {self.table}(a_id, user_id) VALUES(%s,%s)"
        self.cursor.execute(sql, (qid,uid))
        self.conn.commit()

    def delete_saved_question(self,qid):
        sql = f"DELETE FROM {self.table} WHERE sa_aid= %s"
        self.cursor.execute(sql,(qid,))