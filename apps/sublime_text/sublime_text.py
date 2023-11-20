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
    # Mark actions

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
    # Windows and tabs

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
    # Windows and tabs

    def tab_jump(number: int):
        if number <= 9:
            actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    # Marks

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
    # Line manipulation

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

@ctx.action_class("user")
class FindAndReplaceActions:
    # Find and replace
    def find(text: str):
        actions.key("cmd-f")
        actions.insert(text)

    def find_next():
        actions.key("cmd-g")

    def find_previous():
        actions.key("cmd-shift-g")

    def find_everywhere(text: str):
        actions.key("cmd-shift-f")
        actions.insert(text)

    def find_toggle_match_by_case():
        actions.key("alt-cmd-c")

    def find_toggle_match_by_word():
        actions.key("alt-cmd-w")

    def find_toggle_match_by_regex():
        actions.key("alt-cmd-r")

    def replace(text: str):
        actions.key("alt-cmd-f")

    def replace_everywhere(text: str):
        actions.key("ctrl-alt-enter")

    def replace_confirm():
        actions.key("alt-cmd-e")

    def replace_confirm_all():
        actions.key("ctrl-alt-enter")

    def select_previous_occurrence(text: str):
        actions.key("cmd-f")
        actions.insert(text)
        actions.key("shift-enter")
        actions.key("escape")

    def select_next_occurrence(text: str):
        actions.key("cmd-f")
        actions.insert(text)
        actions.key("enter")      
        actions.key("escape")
