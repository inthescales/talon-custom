from talon import Context, Module, actions

mod = Module()

# Context matching
ctx = Context()
ctx.matches = r"""
os: mac
app: sublime_text
"""

@mod.action_class
class Actions:
    def mark_set():
        """Set the mark"""

    def mark_clear():
        """Clear any set mark"""

    def mark_select():
        """Select to the mark"""

    def mark_delete():
        """Delete to the mark"""

    def mark_swap():
        """Reverse lines of mark and cursor"""

@ctx.action_class("app")
class AppActions:
    def preferences():
        actions.key("cmd-,")

    def tab_next():
        actions.key("cmd-shift-]")

    def tab_previous():
        actions.key("cmd-shift-[")

    def tab_open():
        actions.key("cmd-n")

    def tab_reopen():
        actions.key("cmd-shift-t")

    def window_open():
        return

    def window_close():
        actions.key("cmd-shift-w")

@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number <= 9:
            actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    def mark_set():
        actions.key("cmd-k cmd-m")

    def mark_clear():
        actions.key("cmd-k cmd-g")

    def mark_select():
        actions.key("cmd-k cmd-a")

    def mark_delete():
        actions.key("cmd-k cmd-w")

    def mark_swap():
        actions.key("cmd-k cmd-x")

@ctx.action_class("edit")
class EditActions:
    def indent_less():
        actions.key("cmd-[")

    def indent_more():
        actions.key("cmd-]")

    def jump_line(n: int):
        actions.key("ctrl-g")
        actions.insert(n)
        actions.key("enter")

    def line_swap_up():
        actions.key("ctrl-cmd-up")

    def line_swap_down():
        actions.key("ctrl-cmd-down")

    def line_clone():
        actions.key("cmd-shift-d")

@ctx.action_class("code")
class CodeActions:
    def toggle_comment():
        actions.key("cmd-/")
