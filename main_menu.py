from tkinter import *
import webbrowser
from tkvideo import tkvideo
import subprocess

class main_window:

    def __init__(self):
        # initialize base variables
        self.root = Tk()
        self.window_size = self.root.geometry("2000x1010")
        self.root.title("Test Version")
        self.welcome_text = Label(self.root, text = "Test Version Entertainment Hub", font = ("Times New Roman", 30))
        self.user1 = "Sven"
        self.user2 = "Julian"
        self.user1_logged_in = False
        self.user2_logged_in = False
        # create image objects
        self.basepath = "/home/pi/python/projects/Assets"
        self.background_image = PhotoImage(file = self.basepath + "/background_pi.png")
        self.background_label = Label(self.root, image = self.background_image)
        self.spotify_image = PhotoImage(file = f"{self.basepath}/spotify_logo.png")
        self.netflix_image = PhotoImage(file = f"{self.basepath}/netflix_logo.png")
        self.games_image = PhotoImage(file = f"{self.basepath}/game_logo.png")
        self.fireplace_button_image = PhotoImage(file = f"{self.basepath}/Fireplace.png")
        self.disney_image = PhotoImage(file = f"{self.basepath}/disney_logo.png")
        self.prime_image = PhotoImage(file = f"{self.basepath}/prime_logo.png")
        self.youtube_image = PhotoImage(file = f"{self.basepath}/youtube_image.png")
        self.pong_button_image = PhotoImage(file = f"{self.basepath}/pong.png")
        self.game_background = PhotoImage(file = f"{self.basepath}/game_window_background.png")
        self.user1_image = PhotoImage(file = f"{self.basepath}/user1.png")
        self.user2_image = PhotoImage(file = f"{self.basepath}/user2.png")
        self.power_button_image = PhotoImage(file = f"{self.basepath}/power_button.png")
        # create buttons
        self.spotify_button = Button(self.root, image = self.spotify_image, width = 200, height = 200, command = self.open_spotify)
        self.netflix_button = Button(self.root, image = self.netflix_image, width = 200, height = 200, command = self.open_netflix)
        self.game_button = Button(self.root, image = self.games_image, width = 200, height = 200, command = self.main_games_window)
        self.fireplace_button = Button(self.root, image = self.fireplace_button_image, width = 200, height = 200, command = self.fire)
        self.disney_plus_button = Button(self.root, image = self.disney_image, width = 200, height = 200, command = self.open_disney)
        self.prime_button = Button(self.root, image = self.prime_image, width = 200, height = 200, command = self.open_prime)
        self.youtube_button = Button(self.root, image = self.youtube_image, width = 200, height = 200, command = self.open_youtube)
        self.user1_button = Button(self.root, image = self.user1_image, width = 100, height = 100, command = lambda m = f"{self.user1} logged in": self.show_logged_in_user(m))
        self.user2_button = Button(self.root, image = self.user2_image, width = 100, height = 100, command = lambda m = f"{self.user2} logged in": self.show_logged_in_user(m))
        self.power_button = Button(self.root, image = self.power_button_image, width = 100, height = 100, command = self.power_off)
        #create description labels
        self.spotify_label = Label(self.root, text = "Spotify")
        self.netflix_label = Label(self.root, text = "Netflix")
        self.disney_label = Label(self.root, text = "Disney +")
        self.prime_label = Label(self.root, text = "Prime Video")
        self.fireplace_label = Label(self.root, text = "Fireplace")
        self.games_label = Label(self.root, text = "Games")
        self.youtube_label = Label(self.root, text = "YouTube")
        self.login_label = Label(self.root, text = "CLICK TO LOG IN USER")

    def place_items_on_window(self):
        self.background_label.place(y = 0, x = 0)
        # place buttons on screen
        self.welcome_text.grid(column = 0, row = 1, columnspan = 6)
        self.spotify_button.grid(column = 0, row = 2)
        self.netflix_button.grid(column = 1, row = 2)
        self.disney_plus_button.grid(column = 2, row = 2)
        self.prime_button.grid(column = 3, row = 2)
        self.fireplace_button.grid(column = 4, row = 2)
        self.game_button.grid(column = 5, row = 2)
        self.youtube_button.grid(column = 6, row = 2)
        self.user1_button.place(y = 900, x = 0)
        self.user2_button.place(y = 900, x = 110)
        self.power_button.place(y = 900, x = 1800)
        # place description labels on screen
        self.spotify_label.grid(column = 0, row = 3)
        self.netflix_label.grid(column = 1, row = 3)
        self.disney_label.grid(column = 2, row = 3)
        self.prime_label.grid(column = 3, row = 3)
        self.fireplace_label.grid(column = 4, row = 3)
        self.games_label.grid(column = 5, row = 3)
        self.youtube_label.grid(column = 6, row = 3)
        self.login_label.place(y = 878, x = 50)


    def loop_main_window(self):
        self.root.mainloop()

    def open_spotify(self):
        subprocess.call("/home/pi/chrome-pjibgclleladliembfgfagdaldikeohf-Default.desktop")

    def open_netflix(self):
        webbrowser.open("https://netflix.com")

    def open_disney(self):
        webbrowser.open("https://disneyplus.com")

    def open_prime(self):
        webbrowser.open("https://www.amazon.de/Amazon-Video/b?ie=UTF8&node=3010075031")

    def open_youtube(self):
        webbrowser.open("https://youtube.com")

    def fire(self):
        root2 = Toplevel()
        root2.geometry("2000x1010")
        root2.title("Fireplace")
        fireplace_video_label = Label(root2)
        fireplace_video_label.grid(column = 0, row = 0)
        fireplace_player = tkvideo(self.basepath + "/lagerfeuer.mp4", fireplace_video_label, loop = 10, size = (2000, 1010))
        fireplace_player.play()

    def main_games_window(self):
        root3 = Toplevel()
        root3.geometry("2000x1010")
        root3.title("Games Menu")
        game_background_label= Label(root3, image = self.game_background)
        game_background_label.place(y = 0, x = 0)
        games_text = Label(root3, text = "CHOOSE YOUR GAME")
        games_text.grid(column = 0, row = 0, columnspan = 9)
        pong_button = Button(root3, image = self.pong_button_image, width = 200, height = 200)
        pong_button.grid(column = 0, row = 1)

    def show_logged_in_user(self, logged_in_user):
        user_label = Label(self.root, text = logged_in_user, width = 15, height = 2)
        user_label.place(y = 500, x = 800)

        if logged_in_user == self.user1:
             self.user1_logged_in = True
             self.user2_logged_in = False

        elif logged_in_user == self.user2:
            self.user1_logged_in = False
            self.user2_logged_in = True
            
    def power_off(self):
        subprocess.run(["shutdown", "+0"])
        exit()


window1 = main_window()
window1.place_items_on_window()
window1.loop_main_window()
