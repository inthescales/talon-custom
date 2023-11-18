from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
app: windows explorer
"""

@ctx.action_class("user")
class UserActions:
    def file_rename():
        actions.key("f2")

    def file_delete():
        actions.key("delete")

    def file_open():
        actions.key("enter")
    
    def new_folder():
        actions.key("ctrl-shift-n")
