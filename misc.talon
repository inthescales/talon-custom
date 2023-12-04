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
