from tkinter import *
import webbrowser

class main_window:

    def __init__(self):
        self.root = Tk()
        self.window_size = self.root.geometry("1200x700")
        self.welcome_text = Label(self.root, text = "Welcome Text", font = ("Times New Roman", 30))
        self.spotify_image = PhotoImage(file = r"C:\Users\Sven\Desktop\Programming\Python\Projects\Raspberry_pi\Ent_System\spotify_logo.png")
        self.spotify_button = Button(self.root, image = self.spotify_image, width = 250, height = 200, command = self.open_spotify)
        self.netflix_image = PhotoImage(file = r"C:\Users\Sven\Desktop\Programming\Python\Projects\Raspberry_pi\Ent_System\netflix_logo.png")
        self.netflix_button = Button(self.root, image = self.netflix_image, width = 250, height = 200)
        self.game_button = Button(self.root, text = "Games", width = 32, height = 13)
        

    def place_items_on_window(self):
        self.welcome_text.pack()
        self.spotify_button.place(x = 100, y = 130)
        self.netflix_button.place(x = 480, y = 130)
        self.game_button.place(x = 860, y = 130)

    def loop_main_window(self):
        self.root.mainloop()

    def open_spotify(self):
        webbrowser.open("https://open.spotify.com")

window1 = main_window()
window1.place_items_on_window()
window1.loop_main_window()
