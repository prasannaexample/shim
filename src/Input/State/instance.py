class instance():
    def __init__(self, filename):
        self.lines = [line for line in open(filename, 'r')]
        self.cursor_x, self.cursor_y = 0, 0
        self.curr_top = 0
    # line numbers are 0 indexed
    def get_lines(self):
        return self.lines
    def get_cursor(self):
        return self.cursor_x, self.cursor_y
