# import os

from talon import Context, Module, actions #, ui
# from talon.mac import applescript

mod = Module()
ctx = Context()
ctx.matches = r"""
app: finder
"""

@mod.action_class
class UserActions:
    def open_path_dialog():
        """Open dialogue for moving to a specific path"""

    def send_to_new_folder():
        """Send all selected files to a new folder"""

    def file_copy_path():
        """Copy the path of the selected file"""

    def file_move():
        """Move a file that has been copied to the clipboard"""

@ctx.action_class("user")
class UserActions:
    def open_path_dialog():
        actions.key("cmd-shift-g")

    def send_to_new_folder():
        actions.key("ctrl-cmd-n")

    def file_rename():
        actions.key("enter")

    def file_delete():
        actions.key("cmd-delete")

    def file_open():
        actions.key("cmd-o")
    
    def new_folder():
        actions.key("shift-cmd-n")

    def file_copy_path():
        actions.key("alt-cmd-c")

    def file_move():
        actions.key("cmd-alt-v")