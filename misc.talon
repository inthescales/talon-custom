slap: key(enter)
quit: key(escape)
oops: user.undo()

# Path handling

path <user.system_path>: insert(system_path)

# Desktops

desk left: key("ctrl-left")
desk right: key("ctrl-right")

window pass left: user.window_move_desktop_left()
window pass right: user.window_move_desktop_right()

# Testing

add string:
    key(right)
    key(,)
    key(space)
    insert("\"\"")
    key(left)

fall: key(alt-left)
spring: key(alt-right)
level:
    key(alt-right)
    key(alt-left)

scrup: mimic("scroll up")
scrown: mimic("scroll down")

nudge up: user.rango_command_without_target("scrollUpPage", 0.2)
nudge down: user.rango_command_without_target("scrollDownPage", 0.2)
nudge left: user.rango_command_without_target("scrollLeftPage", 0.2)
nudge right: user.rango_command_without_target("scrollRightPage", 0.2)

make: insert("make")
make clean: insert("make clean")

# slack needs support for things like fall and spring
