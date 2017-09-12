#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class Handler:
	pass
def close(*args):
	Gtk.main_quit()
	quit()
builder = Gtk.Builder()
builder.add_from_file("")
builder.connect_signals(Handler())
window = builder.get_object("window1")
window.connect("destroy", close )
window.show_all()
Gtk.main()
