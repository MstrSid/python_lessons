from classes.Comment import Comment

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
