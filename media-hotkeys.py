import gi
gi.require_version('Gtk', '3.0')
gi.require_version('RB', '3.0')
from gi.repository import Gtk, RB, GObject, Peas, Gio


class MediaHotkeysPlugin(GObject.Object, Peas.Activatable):
    __gtype_name__ = 'MediaHotkeysPlugin'
    object = GObject.Property(type=GObject.Object)

    def __init__(self):
        super(MediaHotkeysPlugin, self).__init__()

    def do_activate(self):
        shell = self.object
        self.shell = shell
        self.player = shell.props.shell_player

        # self.action_previous = Gio.SimpleAction.new("previous", None)
        self.action_next = Gio.SimpleAction.new("next", None)

        # self.action_previous.connect("activate", self.on_previous)
        self.action_next.connect("activate", self.on_next)

        # self.shell.props.window.add_action(self.action_previous)
        self.shell.props.window.add_action(self.action_next)

        app = Gtk.Application.get_default()
        # app.set_accels_for_action("win.previous", ["F9"])
        app.set_accels_for_action("win.next", ["F10"])

    def do_deactivate(self):
        # self.shell.props.window.remove_action("previous")
        self.shell.props.window.remove_action("next")

    def on_previous(self, *_):
        self.player.do_previous()

    def on_next(self, *_):
        self.player.do_next()
