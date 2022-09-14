#!/usr/bin/python3
from gi.repository import Gtk, Gdk

SCREEN_RES_W = 800
SCREEN_RES_H = 480

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(self)

        win = self.builder.get_object("win_main")
        win.set_default_size(SCREEN_RES_W, SCREEN_RES_H)
        win.set_position(Gtk.WindowPosition.CENTER)


        provider = Gtk.CssProvider()
        provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default (), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def quit(self, button):
        Gtk.main_quit()

MainWindow()