import os
from gi.repository import Gtk

class Application(object):
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        self._create_main_window()
        
    def _create_main_window(self):
        self.window = Gtk.Window()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_title("%s v%s" % (self.package_name, self.version))
        self.window.set_icon_name(self.package)
        path = os.path.join(self.appdatadir, "pixmaps", "hello_earth.png")
        image = Gtk.Image.new_from_file(path)
        self.window.add(image)
        
    def run(self):
        self.window.show_all()
        Gtk.main()
