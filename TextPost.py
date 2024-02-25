from Posts import Posts


class TextPost(Posts):

    def __init__(self, user, text):  # fixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        super().__init__(user)
        self.text = text

    def print_info(self):
        print(f"{self._user._username} published a post:")
        print(f"\"{self.text}\"")
        print()
