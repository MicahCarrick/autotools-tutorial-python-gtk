import os
from gi.repository import Gtk

class Application(object):
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        self._create_main_window()
    
    def _create_main_window(self):
        builder = Gtk.Builder()
        ui_file = os.path.join(self.pkgdatadir, "ui", "main_window.ui")
        builder.add_from_file(ui_file)
        builder.connect_signals(self)
        self.window = builder.get_object("main_window")
        self.window.set_title("%s v%s" % (self.package, self.version))
        self.window.set_icon_name(self.package)
    
    def quit(self, widget=None, data=None):
        Gtk.main_quit()
        
    def run(self):
        self.window.show_all()
        Gtk.main()
