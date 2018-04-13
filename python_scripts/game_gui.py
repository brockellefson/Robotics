import tkinter as tk


class GameGui():
    def __init__(self, debug=False):
        # root widget
        self.main_window = tk.Tk()

        # finding and setting window size to current resolution
        self.window_width = self.main_window.winfo_screenwidth()
        self.window_height = self.main_window.winfo_screenheight()
        self.main_window.geometry("%dx%d%+d%+d" % (self.window_width, self.window_height, 0, 0))
        if debug:
            print('using resolution: {} x {}'.format(self.window_width, self.window_height))

        self.create_hud(self.main_window)

    def create_hud(self, main_window):
        can = tk.Canvas(main_window, bg='#000000', width=0.8 * self.window_width, height=0.8 * self.window_height)
        can.grid(row=0, column=0)

        test_button = tk.Button(text='push me')
        test_button.grid(row=1, column=0)

    # we should discuss and maybe draw some pictures
    # of how we want the hud to look and behave

    def mainloop(self):
        self.main_window.mainloop()

    def quit(self):
        self.main_window.destroy()


def main():
    a = GameGui(True)
    a.mainloop()


if __name__ == '__main__':
    main()
