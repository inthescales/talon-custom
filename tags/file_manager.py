from talon import Module

mod = Module()

@mod.action_class
class FileManagerActions:
    def file_rename():
        """Rename a selected file"""

    def file_delete():
        """Delete a selected file or files"""

    def new_folder():
        """Create a new folder"""
