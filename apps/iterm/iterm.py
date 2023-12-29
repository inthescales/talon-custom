from talon import Context, actions

ctx = Context()

ctx.matches = r"""
app: iterm2
"""

@ctx.action_class("app")
class UserActions:
    def tab_next():
        actions.key("cmd-shift-]")

    def tab_previous():
        actions.key("cmd-shift-[")
