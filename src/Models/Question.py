
class Question:
    
    def __init__(self, cursor, cnx):
        self.table = "questions" # SQL TABLE
        # ========== MYSQL CONNECTIONS ==========
        self.cursor = cursor
        self.cnx = cnx

    # ========== UPLOAD A QUESTION ==========
    def upload_question(self, question, userid):
        sql = "INSERT INTO questions(question,user_id) VALUES(%s, %s)"
        try:
            self.cursor.execute(sql,(question, userid))
            self.cnx.commit()
        except: 
            return False

    # ========== GET ALL QUESTIONS ==========
    def get_all_question(self):
        try:
            self.cursor.execute("SELECT * FROM questions ORDER BY created_at DESC")
            questions = self.cursor.fetchall()
            return questions
        except:
            return False
       
    # ==========  GET QUESTION BY QUESTION ID ==========
    def get_question(self, id):
        sql = f"SELECT * FROM {self.table} WHERE qid = %s"
        try:
            self.cursor.execute(sql,(id,))
            questions = self.cursor.fetchall()
            return questions
        except:
            return False

    # ========== DELETE questions and all its answers ==================
    def delete_question_answer(self,qid):
        try:
            self.cursor.execute("DELETE FROM answers WHERE q_id=%s", (qid,))
            self.cnx.commit()
            self.cursor.execute("DELETE FROM questions WHERE qid=%s", (qid,))
            self.cnx.commit()
        except:
            self.cnx.rollback()
    
    # ==================  UPDATE QUESTION =================
    def update_question(self,question,qid):
        sql = f"UPDATE {self.table} SET question=%s WHERE qid=%s"
        self.cursor.execute(sql,(question,qid))
        self.cnx.commit()
    