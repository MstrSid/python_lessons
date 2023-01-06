from classes.Comment import Comment


class ExtComment(Comment):
    def __init__(self, date, text):
        super().__init__(text)
        self.date = date

    def get_info(self):
        return f"Text: {self.text}, upvote: {self.upvote()}, date: {self.date}"

    def __eq__(self, other):
        return True if self.text == other.text and self.qty == other.qty and self.date == other.date else False
