from tkinter import *
import webbrowser
from tkvideo import tkvideo

class main_window:

    def __init__(self):
        self.basepath = "/home/pi/python/Assets"
        self.root = Tk()
        self.window_size = self.root.geometry("1270x700")
        self.welcome_text = Label(self.root, text = "Test Version Entertainment Hub", font = ("Times New Roman", 30))
        self.spotify_image = PhotoImage(file = self.basepath + "/spotify_logo.png")
        self.spotify_button = Button(self.root, image = self.spotify_image, width = 200, height = 200, command = self.open_spotify)
        self.netflix_image = PhotoImage(file = self.basepath + "/netflix_logo.png")
        self.netflix_button = Button(self.root, image = self.netflix_image, width = 200, height = 200, command = self.open_netflix)
        self.games_image = PhotoImage(file = self.basepath + "/game_logo.png")
        self.game_button = Button(self.root, image = self.games_image, width = 200, height = 200)
        self.fireplace_button_image = PhotoImage(file = self.basepath + "/Fireplace.png")
        self.fireplace_button = Button(self.root, image = self.fireplace_button_image, width = 200, height = 200, command = self.fire)
        self.disney_image = PhotoImage(file = self.basepath + "/disney_logo.png")
        self.disney_plus_button = Button(self.root, image = self.disney_image, width = 200, height = 200, command = self.open_disney)
        self.prime_image = PhotoImage(file = self.basepath + "/prime_logo.png")
        self.prime_button = Button(self.root, image = self.prime_image, width = 200, height = 200, command = self.open_prime)

    def place_items_on_window(self):
        self.welcome_text.grid(column = 0, row = 0, columnspan = 6)
        self.spotify_button.grid(column = 0, row = 1)
        self.netflix_button.grid(column = 1, row = 1)
        self.disney_plus_button.grid(column = 2, row = 1)
        self.prime_button.grid(column = 3, row = 1)
        self.fireplace_button.grid(column = 4, row = 1)
        self.game_button.grid(column = 0, row = 2)

    def loop_main_window(self):
        self.root.mainloop()

    def open_spotify(self):
        webbrowser.open("https://open.spotify.com")

    def open_netflix(self):
        webbrowser.open("https://netflix.com")

    def open_disney(self):
        webbrowser.open("https://disneyplus.com")

    def open_prime(self):
        webbrowser.open("https://www.amazon.de/Amazon-Video/b?ie=UTF8&node=3010075031")

    def fire(self):
        root2 = Toplevel()
        root2.geometry("1270x700")
        fireplace_video_label = Label(root2)
        fireplace_video_label.grid(column = 0, row = 0)
        fireplace_player = tkvideo(self.basepath + "/Fireplace.mp4", fireplace_video_label, loop = 1, size = (1270, 700))
        fireplace_player.play()

window1 = main_window()
window1.place_items_on_window()
window1.loop_main_window()
