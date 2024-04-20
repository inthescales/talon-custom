snail: insert("@")
noodle: insert("?")
en dash: insert("–")
em dash: insert("—")

args empty: insert("()")

(quote pair | quotation):
    insert("\"\"")
    key(left)

(cite pair | citation):
    insert("''")
    key(left)

hug | cradle:
    insert("()")
    key(left)

shackle | shackles | subscript:
    insert("[]")
    key(left)

doily:
    insert("{}")
    key(left)

diamond:
    insert("<>")
    key(left)

curly: insert("{")
right curly: insert("}")

empty (hug | cradle): insert("()")
empty shackles: insert("[]")

Orion's belt: insert("...")

# Special characters

round air: insert("ɑ")
broken odd: insert("ɔ")
curved each: insert("ɛ")
schwa: insert("ə")
long mark: insert("ː")

# Diacritics

accent: key("alt-e")
macron: key("alt-a")
(palatal | palate): key("alt-w")
chapel: key("alt-6")
