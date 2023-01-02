from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    # Search for the image to load on the screen
    def search_image(self):
        # Get user query from the text input
        search_query = self.manager.current_screen.ids.user_query.text

        # Get the wikipedia page and the first image link
        pg = wikipedia.page(search_query, 'features="html.parser"')
        print(pg.images)
        image_link = pg.images[0]
        return image_link

    # Download the image
    def download_image(self):
        # Download the image
        req = requests.get(self.search_image())
        imgpath = 'image.jpg'
        with open(imgpath, 'wb') as file:
            file.write(req.content)
        return imgpath

    # Load the image on the screen
    def set_image(self):
        self.manager.current_screen.ids.foto.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
