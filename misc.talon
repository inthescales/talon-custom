quit: key(escape)
oops: user.undo()

# Line manipulation

snatch: mimic("cut line")

# Path handling

path <user.system_path>: insert(system_path)

# Desktops

desk left: key("ctrl-left")
desk right: key("ctrl-left")

window pass left: user.window_move_desktop_left()
window pass right: user.window_move_desktop_right()
