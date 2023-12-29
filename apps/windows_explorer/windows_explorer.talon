app: windows explorer
-
# Window
go (address | path): key(alt-d)
go search: key(ctrl-e)

copy (address | path):
	key(alt-d)
	key(ctrl-c)

# New objects
new text:
	key(shift-f10)
	key(w)
	key(t)

# File commands
rename: user.file_rename()
delete: user.file_delete()
properties: key(alt-enter)
