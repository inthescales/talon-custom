from talon import Context, Module, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: mac
app: sublime_text
"""


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

mod = Module()

@mod.action_class
class Actions:
