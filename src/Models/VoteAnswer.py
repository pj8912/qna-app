class VoteAnswer:

    def __init__(self, cursor, cnx):
        self.table = "vote_answers"
        self.cursor = cursor
        self.cnx = cnx


    def upvote(self, aid, uid):
        sql = f"INSERT INTO {self.table}(a_id,user_id) VALUES(%s,%s)"
       try:
           self.cursor.execute(sql,(aid,uid))
           self.commit()
       except:
           return False



    def downvote(self, vote_id):
         sql = f"DELETE FROM {self.table} WHERE aqid=%s"
       try:
           self.cursor.execute(sql,(vote_id,))
       except:
           return False
