app: chrome
-
hunt this: user.find("")
hunt this (pace | paste):
    user.find("")
    sleep(25ms)
    edit.paste()
hunt this <user.text>: user.find(text)
hunt all: user.find_everywhere("")
hunt all (pace | paste):
    user.find_everywhere("")
    sleep(25ms)
    edit.paste()
hunt all <user.text>: user.find_everywhere(text)
hunt case: user.find_toggle_match_by_case()
hunt word: user.find_toggle_match_by_word()
hunt expression: user.find_toggle_match_by_regex()
hunt next: user.find_next()
hunt previous: user.find_previous()

next: user.find_next()
sup: user.find_previous()

go last <user.text> [over]:
    user.select_previous_occurrence(text)
    sleep(100ms)
    edit.right()
go last clip:
    user.select_previous_occurrence(clip.text())
    sleep(100ms)
    edit.right()
go next <user.text> [over]:
    user.select_next_occurrence(text)
    edit.right()
go next clip:
    user.select_next_occurrence(clip.text())
    edit.right()
