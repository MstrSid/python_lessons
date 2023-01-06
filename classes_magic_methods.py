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


first_comment = Comment('first')
first_comment.upvote()
first_comment.upvote()
second_comment = Comment('second')
second_comment.upvote()
print(Comment.total)

print(first_comment + second_comment)

some_comment = Comment("some")
some_comment.upvote()
another_comment = Comment("some")
another_comment.upvote()

print(some_comment == another_comment)
