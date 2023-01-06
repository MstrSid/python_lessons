class Comment:
    total = 0

    def __init__(self, text):
        self.text = text
        self.qty = 0
        Comment.total += 1

    def upvote(self):
        self.qty += 1

    def __add__(self, other):
        return {'text': f"{self.text} {other.text}", 'total votes': self.qty + other.qty}

    def __eq__(self, other):
        return True if self.text == other.text and self.qty == other.qty else False
