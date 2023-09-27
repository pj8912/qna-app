class Answer:
    
    def __init__(self, cursor,cnx):
        self.table = "answers"
        # ==== MSYQL CONFIG ==== 
        self.cursor = cursor
        self.cnx = cnx
    
    # ======== UPLOAD ANSWER ============
    def upload_answer(self, qid, answer, uid):
        try:
            self.cursor.execute("INSERT INTO"+self.table+"(q_id, answer, user_id) VALUES(%s, %s, %s)")
            self.cnx.commit()
        except:
            return False
    

    # ===== DELETE ANSWER BY ANSWER ID =========
    def delete_answer(self, aid):
        sql = f"DELETE FROM{self.table}WHERE aid=%s"
        try:
            self.cursor.execute(sql, (aid,))
            self.cnx.commit()
        except:
            return False

    # ===== GET ALL ANSWERS POSTED BY USER =========
    def get_my_answers(self,uid):
        try:
            self. cursor.execute("SELECT * FROM answers WHERE user_id= %s", (uid, ))
            answers = self.cursor.fetchall()
            return answers
        except:
            return False
        
    # ====== GET ANSWER BY QUESTION ID ===========
    def get_answers(self, qid):
        try:
            self.cursor.execute("SELECT * FROM answers WHERE q_id=%s", (qid,))
            answers = self.cursor.fetchall()
            return answers
        except:
            return False


    # ======= UPDATE ANSWER =======
    def update_answer(self,aid,answer):
        sql = "UPDATE TABLE {self.table} SET answer=%s WHERE aid=%s"
        try:
            self.cursor.execute(sql, (answer,aid))
            self.cnx.commit()
        except:
            return False
