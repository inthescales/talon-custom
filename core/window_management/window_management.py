from talon import Context, Module, actions, app

mod = Module()

@mod.action_class
class FlipActions:
    def flip():
        """Opens the last used application"""
        if app.platform == "windows":
            actions.key("alt-tab")
        elif app.platform == "mac":
            actions.key("cmd-tab")

    def fullscreen():
        """Makes the currently focused application fullscreen"""
        if app.platform == "windows":
            actions.key("alt-space")
            actions.key("x")
        elif app.platform == "mac":
            actions.key("cmd-ctrl-f")

    def end_fullscreen():
        """Ends fullscreen for the application""" 
        if app.platform == "windows":
            actions.key("alt-space")
            actions.key("r")
        elif app.platform == "mac":
            actions.key("cmd-ctrl-f")
