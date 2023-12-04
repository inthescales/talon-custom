os: mac
tag: terminal
-
# Quick actions

rerun that: user.terminal_run_last()

# Editing text
clear word:
    key(alt-right)
    key(alt-backspace)

clear word right:
    key(alt-delete)

clear word left:
    key(alt-backspace)

chop line: key(ctrl-k)
paste chop: key(ctrl-y)

# Process management
kill (this | that | it): key(ctrl-c)

(background | suspend): key(ctrl-z)

foreground | resume:
    insert("fg")
    key(enter)