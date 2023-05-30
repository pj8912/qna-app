class Answer:
    
    def __init__(self, cursor,cnx):
        self.table = "answers"
        self.cursor = cursor
        self.cnx = cnx
    
    def upload_answer(self, qid, answer, uid):
        self.cursor.execute("INSERT INTO"+self.table+"(q_id, answer, user_id) VALUES(%s, %s, %s)")
        cnx.commit()
    
    def delete_answer(self, aid):
        self.cursor.execute("DELETE FROM"+self.table+"WHERE aid=%s", (aid,))
   

   def get_my_answers(self,uid):
       self. cursor.execute("SELECT * FROM answers WHERE user_id= %s", (session['u_id'], ))
       answers = self.cursor.fetchall()
       return answers
        
    
   def get_answers(self, qid):
       self.cursor.execute("SELECT * FROM answers WHERE q_id=%s", (id,))
       answers = self.cursor.fetchall()
       return answers

