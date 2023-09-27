class VoteAnswer:

    def __init__(self, cursor, cnx):
        self.table = "vote_answers"
        self.cursor = cursor
        self.cnx = cnx


    def upvote(self, aid, uid):
        pass

    def downvote(self, vote_id):
        pass