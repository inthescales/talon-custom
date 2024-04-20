quit: key(escape)
oops: user.undo()

# Path handling

path <user.system_path>: insert(system_path)

# Desktops

desk left: key("ctrl-left")
desk right: key("ctrl-right")

window pass left: user.window_move_desktop_left()
window pass right: user.window_move_desktop_right()

# Editing

sink: user.delete_right()

fall: key(alt-left)
spring: key(alt-right)
level:
    key(alt-right)
    key(alt-left)

word wrap backtick:
    edit.word_left()
    insert("`")
    edit.word_right()
    insert("`")

add string:
    key(right)
    key(,)
    key(space)
    insert("\"\"")
    key(left)

again: edit.redo()

# Browser

nudge up: user.rango_command_without_target("scrollUpPage", 0.2)
nudge down: user.rango_command_without_target("scrollDownPage", 0.2)
nudge left: user.rango_command_without_target("scrollLeftPage", 0.2)
nudge right: user.rango_command_without_target("scrollRightPage", 0.2)

# Terminal

make: insert("make ")
make clean: insert("make clean")

# Misc

scrup: mimic("scroll up")
scrown: mimic("scroll down")

screen lock: key("ctrl-cmd-q")

# slack needs support for things like fall and spring
