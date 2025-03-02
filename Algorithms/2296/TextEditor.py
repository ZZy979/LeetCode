class TextEditor:

    def __init__(self):
        self.text = []
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.text[self.cursor:self.cursor] = text
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        n = min(self.cursor, k)
        del self.text[self.cursor - n:self.cursor]
        self.cursor -= n
        return n

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        return ''.join(self.text[max(0, self.cursor - 10):self.cursor])

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.text), self.cursor + k)
        return ''.join(self.text[max(0, self.cursor - 10):self.cursor])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
