import tkinter as tk

class Animation:

    def animat(self):
        root = tk.Tk()

        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        x = int(window_width / 2)
        y = int(window_height / 2)
        root.geometry("%dx%d%+d%+d" % (window_width, window_height, x, y))

        root.mainloop()

    def run(self):
        self.animat()