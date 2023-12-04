elpar: insert("(")
arpar: insert(")")
elsquare: insert("[")
arsquare: insert("]")
elbrace: insert("{")
arbrace: insert("}")
elang: insert("<")
arang: insert(">")

snail: insert("@")

args empty: insert("()")

(quote pair | quotation):
    insert("\"\"")
    key(left)

(cite pair | citation):
    insert("''")
    key(left)

squares:
    insert("[]")
    key(left)

doily:
    insert("{}")
    key(left)

diamond:
    insert("<>")
    key(left)

# Special characters

# ash: insert("æ")
long ash: insert("ǣ")
# thorn: insert("þ")
# snithe: insert("ð")
# theta: insert("θ")
# gamma: insert("ɣ")
# shin: insert("ʃ")
# jaque: insert("ʒ")

palatal cap: insert("ċ")
palatal gust: insert("ġ")

round air: insert("ɑ")
broken odd: insert("ɔ")
curved each: insert("ɛ")
schwa: insert("ə")

long mark: insert("ː")
macron: key("alt-a")
