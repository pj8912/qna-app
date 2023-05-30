
class Question:
    
    def __init__(self, cursor, cnx):
        self.table = "questions"
        self.cursor = cursor
        self.cnx = cnx

    
    def upload_question(self, uid):
        self.cursor.execute("INSERT INTO questions(question,user_id) VALUES(%s, %s)", (question, userid))
        self.cnx.commit()


    def get_all_question(self):
        self.cursor.execute("SELECT * FROM questions ORDER BY created_at DESC")
        questions = self.cursor.fetchall()
        return questions

        
