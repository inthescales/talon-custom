from talon import Module, actions, app

mod = Module()

@mod.action_class
class MiscActions:
    def undo():
        """Undoes the previous action"""
        
        if app.platform == "windows":
            actions.key("ctrl-z")
        elif app.platform == "mac":
            actions.key("cmd-z")
