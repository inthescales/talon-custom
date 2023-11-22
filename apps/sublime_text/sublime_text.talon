app: sublime_text
os: mac
-
tag(): user.find_and_replace
tag(): user.line_commands
tag(): user.splits
tag(): user.tabs

# Mark manipulation

mark set: user.mark_set()
mark (unset | remove): user.mark_clear()

select mark: user.mark_select()
clear mark: user.mark_delete()
swap mark: user.mark_swap()

# Advanced search

go symbol [<user.text>]: user.search_symbol(text or "")
go symbol all [<user.text>]: user.search_symbol_everywhere(text or "")
go anything [<user.text>]: user.search_anything(text or "")

# File manipulation

# Clean these up later
file new:
    app.tab_open()
    key("cmd-shift-s")    
file save: key("cmd-s")
file save as: key("cmd-shift-s")
file save all: key("alt-cmd-sb")
file open: key("cmd-o")
