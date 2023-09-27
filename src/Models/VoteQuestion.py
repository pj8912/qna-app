class VoteQuestion:
    
    def __init__(self, cursor, cnx):
        self.table = "vote_answers"
        # mysql configuration
        self.cursor = cursor
        self.cnx = cnx

    def upvote(self, qid, uid):
        pass

    def downvote(self, vote_id):
        pass