scrap [line] <number>:
    user.select_range(number, number)
    edit.delete()
    edit.delete()
scrap <number> through <number>:
    user.select_range(number_1, number_2)
    edit.delete()
    edit.delete()
chop [line] <number>:
    user.select_range(number, number)
    edit.cut()
    edit.delete()
chop [line] <number> through <number>:
    user.select_range(number_1, number_2)
    edit.cut()
    edit.delete()
slip <number>:
    edit.jump_line(number)
    key("enter")
    key("up")
wedge <number>:
    edit.jump_line(number)
    key("enter")
    key("up")    
    edit.paste()
