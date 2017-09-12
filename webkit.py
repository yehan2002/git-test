#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('WebKit', '3.0')
from gi.repository import WebKit
class Handler:
	def on_button1_clicked(self, *args):
		Gtk.main_quit()
def close(*args):
	Gtk.main_quit()
	quit()
builder = Gtk.Builder()
web_view = WebKit.WebView()
web_view.open("file:///home/yehan/Desktop/eyecare/index.html")
builder.add_from_file("/home/yehan/Desktop/eyecare/s.glade")
builder.connect_signals(Handler())
window = builder.get_object("window1")
window.connect("destroy", close )
viewport1 = builder.get_object("viewport1")
viewport1.add(web_view)
window.fullscreen()
window.set_type_hint(Gdk.WindowTypeHint(2))
window.show_all()
window.set_keep_above(True)
Gtk.main()


