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
