tag: terminal
-
# Homebrew
# TODO: find a smarter way to do these

brew info [<user.prose>]:
    message = prose or ""
    insert("brew info ")
    user.insert_formatted(message, "DASH_SEPARATED")

brew install <user.prose>:
    message = prose or ""
    insert("brew install ")
    user.insert_formatted(message, "DASH_SEPARATED")

brew search [<user.prose>]:
    message = prose or ""
    insert("brew search ")
    user.insert_formatted(message, "DASH_SEPARATED")

brew uninstall [<user.prose>]:
    message = prose or ""
    insert("brew uninstall ")
    user.insert_formatted(message, "DASH_SEPARATED")

brew update:
    insert("brew update")

brew upgrade [<user.prose>]:
    message = prose or ""
    insert("brew upgrade ")
    user.insert_formatted(message, "DASH_SEPARATED")

# Python

python: insert("python3 ")
python two: insert("python")
python three: insert("python3 ")

pip: insert("pip ")
pip three: insert("pip3 ")

# Pyenv

env activate [<user.text>]:
    dir = text or "env"
    insert("source {dir}/bin/activate")
env deactivate: insert("deactivate")
env install requirements [<user.text>]:
    reqs = text or "requirements.txt"
    insert("pip3 install -r {reqs}")

# Lyre's Dictionary

python lyre: insert("python3 lyre.py --test")
python lyre count <number_small>: insert("python3 lyre.py --test -c {number_small}")
python lyre diachron: insert("python3 diachron.py > out.html")

# Sublime Text

sublime: insert("subl ")
