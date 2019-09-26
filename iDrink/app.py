"""
An app that finds fountains
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Idrink(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        label = toga.Label("Siamo furbi")
        main_box.add(label)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Idrink('iDrink', 'it.rainerum.iDrink')
