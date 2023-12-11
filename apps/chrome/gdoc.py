from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

mod.apps.chrome = "app.name: Google Chrome"
mod.apps.chrome = """
os: windows
and app.exe: chrome.exe
"""
mod.apps.chrome = """
os: mac
app.bundle: com.google.Chrome
app.bundle: com.google.Chrome.canary
app.bundle: org.chromium.Chromium
"""
mod.apps.chrome = """
os: linux
app.exe: chrome
app.exe: chromium-browser
app.exe: chromium
"""
mod.apps.chrome = """
os: linux
and app.name: Google-chrome
"""

ctx.matches = r"""
app: chrome
"""


@ctx.action_class('user')
class Actions:
    def find(text: str):
        """Finds text in current editor"""
        print("I'm here now")
        actions.key("cmd-f")        
        actions.insert(text)

    def find_next():
        actions.key("cmd-g")

    def find_previous():
        actions.key("cmd-shift-g")

    def find_everywhere(text: str):
        actions.key("cmd-shift-f")
        actions.insert(text)

    def select_previous_occurrence(text: str):
        """Selects the previous occurrence of the text, and suppresses any find/replace dialogs."""
        actions.key("cmd-f")
        actions.insert(text)
        actions.key("shift-enter")
        actions.key("escape")


    def select_next_occurrence(text: str):
        """Selects the next occurrence of the text, and suppresses any find/replace dialogs."""
        actions.key("cmd-f")
        actions.insert(text)
        # actions.key("enter")
        actions.key("escape")


