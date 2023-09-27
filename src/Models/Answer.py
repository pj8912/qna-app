class Answer:
    
    def __init__(self, cursor,cnx):
        self.table = "answers"
        self.cursor = cursor
        self.cnx = cnx
    
    def upload_answer(self, qid, answer, uid):
        self.cursor.execute("INSERT INTO"+self.table+"(q_id, answer, user_id) VALUES(%s, %s, %s)")
        self.cnx.commit()
    
    def delete_answer(self, aid):
        sql = f"DELETE FROM{self.table}WHERE aid=%s"
        self.cursor.execute(sql, (aid,))
        self.cnx.commit()


    def get_my_answers(self,uid):
       self. cursor.execute("SELECT * FROM answers WHERE user_id= %s", (uid, ))
       answers = self.cursor.fetchall()
       return answers
        
    
    def get_answers(self, qid):
       self.cursor.execute("SELECT * FROM answers WHERE q_id=%s", (qid,))
       answers = self.cursor.fetchall()
       return answers

    def update_answer(self,aid,answer):
        sql = "UPDATE TABLE {self.table} SET answer=%s WHERE aid=%s"
        self.cursor.execute(sql, (answer,aid))
        self.cnx.commit()
