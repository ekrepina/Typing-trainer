class Statistics:

    def __init__(self):
        self.time = 0
        self.wpm = 0
        self.errors_count = 0

    def update_wpm(self, window):
        self.wpm = round(int(window.words_button.count) / self.time * 60)

