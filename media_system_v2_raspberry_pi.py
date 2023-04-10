from tkinter import *
import webbrowser
from tkvideo import tkvideo
import subprocess
import customtkinter as ck
from PIL import Image

class main_window:

    def __init__(self):
        # initialize base variables
        self.root = ck.CTk()
        self.window_size = self.root.geometry("1200x900")
        self.root.title("Test Version")
        ck.set_default_color_theme("green")
        self.welcome_text = ck.CTkLabel(self.root, text = "Entertainment Hub", font = ("Arial", 30))
        self.user1 = "Sven"
        self.user2 = "Julian"
        self.user1_logged_in = False
        self.user2_logged_in = False
        #create image objects
        self.button_picturesize = (100, 100)
        self.basepath = "/home/rougeklaire/media_system/Assets"
        #self.background_image = ck.CTkImage(light_image = Image.open(self.basepath + "/background_pi.png"), size = (1200, 900))
        #self.background_label = ck.CTkLabel(self.root, image = self.background_image)
        self.spotify_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/spotify_logo.png"), size = self.button_picturesize)
        self.netflix_image = ck.CTkImage(light_image = Image.open(self.basepath + "/netflix_logo.png"), size = self.button_picturesize)
        self.games_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/game_logo.png"), size = self.button_picturesize)
        self.fireplace_button_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/Fireplace.png"), size = self.button_picturesize)
        self.disney_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/disney_logo.png"), size = self.button_picturesize)
        self.prime_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/prime_logo.png"), size = self.button_picturesize)
        self.youtube_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/youtube_image.png"), size = self.button_picturesize)
        self.pong_button_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/pong.png"), size = self.button_picturesize)
        self.game_background = ck.CTkImage(light_image = Image.open(f"{self.basepath}/game_window_background.png"), size = self.button_picturesize)
        self.user1_image = ck.CTkImage(light_image = Image.open(self.basepath + "/user1.png"), size = self.button_picturesize)
        self.user2_image = ck.CTkImage(light_image = Image.open(self.basepath + "/user2.png"), size = self.button_picturesize)
        self.power_button_image = ck.CTkImage(light_image = Image.open(f"{self.basepath}/power_button.png"), size = self.button_picturesize)
        #create buttons/menus etc.
        self.spotify_button = ck.CTkButton(self.root, text = "Spotify", image = self.spotify_image, width = 200, height = 200, command = self.open_spotify)
        self.netflix_button = ck.CTkButton(self.root, text = "Netflix", image = self.netflix_image, width = 200, height = 200, command = self.open_netflix)
        self.game_button = ck.CTkButton(self.root, text = "Games", image = self.games_image, width = 200, height = 200, command = self.main_games_window)
        self.fireplace_button = ck.CTkButton(self.root, text = "Fireplace", image = self.fireplace_button_image, width = 200, height = 200, command = self.fire)
        self.disney_plus_button = ck.CTkButton(self.root, text = "Disney+", image = self.disney_image, width = 200, height = 200, command = self.open_disney)
        self.prime_button = ck.CTkButton(self.root, text = "Prime Video",image = self.prime_image, width = 200, height = 200, command = self.open_prime)
        self.youtube_button = ck.CTkButton(self.root, text = "YouTube", image = self.youtube_image, width = 200, height = 200, command = self.open_youtube)
        self.user1_button = ck.CTkButton(self.root, text = "Sven", image = self.user1_image, width = 100, height = 100, command = lambda m = f"{self.user1} logged in": self.show_logged_in_user(m))
        self.user2_button = ck.CTkButton(self.root, text = "Julian", image = self.user2_image, width = 100, height = 100, command = lambda m = f"{self.user2} logged in": self.show_logged_in_user(m))
        self.power_button = ck.CTkButton(self.root, text = "power off", image = self.power_button_image, width = 100, height = 100, command = self.power_off)
        self.appearance_mode_menu = ck.CTkOptionMenu(self.root, values = ["System", "Dark", "Light"], command = self.change_appearance_mode)
        #create description labels
        self.spotify_label = ck.CTkLabel(self.root, text = "Spotify")
        self.netflix_label = ck.CTkLabel(self.root, text = "Netflix")
        self.disney_label = ck.CTkLabel(self.root, text = "Disney +")
        self.prime_label = ck.CTkLabel(self.root, text = "Prime Video")
        self.fireplace_label = ck.CTkLabel(self.root, text = "Fireplace")
        self.games_label = ck.CTkLabel(self.root, text = "Games")
        self.youtube_label = ck.CTkLabel(self.root, text = "YouTube")
        self.login_label = ck.CTkLabel(self.root, text = "CLICK TO LOG IN USER", font = ("Arial", 15))
        self.appearance_mode_label = ck.CTkLabel(self.root, text = "Appearance Mode:", anchor="w")

    def place_items_on_window(self):
        #self.background_label.place(y = 0, x = 0)
        #place buttons on screen
        self.welcome_text.grid(column = 0, row = 1, columnspan = 6)
        self.spotify_button.grid(column = 0, row = 2)
        self.netflix_button.grid(column = 1, row = 2)
        self.disney_plus_button.grid(column = 2, row = 2)
        self.prime_button.grid(column = 3, row = 2)
        self.fireplace_button.grid(column = 4, row = 2)
        self.game_button.grid(column = 5, row = 2)
        self.youtube_button.grid(column = 6, row = 2)
        self.user1_button.grid(column = 0, row = 5)
        self.user2_button.grid(column = 1, row = 5)
        self.power_button.grid(column = 6, row = 5)
        self.appearance_mode_menu.grid(row = 3, column = 3)
        # place description labels on screen
        self.spotify_label.grid(column = 0, row = 3)
        self.netflix_label.grid(column = 1, row = 3)
        self.disney_label.grid(column = 2, row = 3)
        self.prime_label.grid(column = 3, row = 3)
        self.fireplace_label.grid(column = 4, row = 3)
        self.games_label.grid(column = 5, row = 3)
        self.youtube_label.grid(column = 6, row = 3)
        self.login_label.grid(column = 0, row = 4, columnspan = 2)
        self.appearance_mode_label.grid(row = 2, column = 3)

    def loop_main_window(self):
            self.root.mainloop()

    def open_spotify(self):
        webbrowser.open("https://open.spotify.com")
        #subprocess.call()

    def open_netflix(self):
        webbrowser.open("https://netflix.com")

    def open_disney(self):
        webbrowser.open("https://disneyplus.com")

    def open_prime(self):
        webbrowser.open("https://www.amazon.de/Amazon-Video/b?ie=UTF8&node=3010075031")

    def open_youtube(self):
        webbrowser.open("https://youtube.com")

    def fire(self):
        root2 = ck.CTkToplevel()
        root2.geometry("2000x1010")
        root2.title("Fireplace")
        fireplace_video_label = ck.CTkLabel(root2)
        fireplace_video_label.grid(column = 0, row = 0)
        fireplace_player = tkvideo(self.basepath + r"\lagerfeuer.mp4", fireplace_video_label, loop = 10, size = (2000, 1010))
        fireplace_player.play()

    def main_games_window(self):
        root3 = ck.CTkToplevel()
        root3.geometry("2000x1010")
        root3.title("Games Menu")
        game_background_label= ck.CTkLabel(root3, image = self.game_background)
        #game_background_label.place(y = 0, x = 0)
        games_text = ck.CTkLabel(root3, text = "CHOOSE YOUR GAME")
        games_text.grid(column = 0, row = 0, columnspan = 9)
        pong_button = ck.CTkButton(root3, image = self.pong_button_image, width = 200, height = 200)
        pong_button.grid(column = 0, row = 1)

    def show_logged_in_user(self, logged_in_user):
        user_label = ck.CTkLabel(self.root, text = logged_in_user, width = 15, height = 2)
        user_label.grid(column = 3, row = 5)

        if logged_in_user == self.user1:
             self.user1_logged_in = True
             self.user2_logged_in = False

        elif logged_in_user == self.user2:
            self.user1_logged_in = False
            self.user2_logged_in = True

    def change_appearance_mode(self, new_appearance_mode: str):
        ck.set_appearance_mode(new_appearance_mode)

    def power_off(self):
        #subprocess.run(["shutdown", "+0"])
        exit()


window1 = main_window()
window1.place_items_on_window()
window1.loop_main_window()
