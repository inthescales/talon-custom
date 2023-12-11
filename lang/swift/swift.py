import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: swift
"""

ctx.lists["user.code_keyword"] = {
    # Declaration
    "import": "import ",
    "var": "var ",
    "let": "let ",
    "class": "class ",
    "struct": "struct ",
    "protocol": "protocol ",
    "enum": "enum ",
    "extension": "extension ",
    "typealias": "typealias ",
    "actor": "actor ",
    "associatedtype": "associatedtype ",
    "final": "final ",
    "public": "public ",
    "private": "private ",
    "open": "open ",
    "internal": "internal ",
    "fileprivate": "fileprivate",
    "static": "static ",
    # "func": "func ",
    "inout": "inout ",
    "async": "async ",
    "throws": "throws ",
    "rethrows": "rethrows ",
    "init": "init ",
    "deinit": "deinit",
    # Statements
    "switch": "switch ",
    "case": "case ",
    "fallthrough": "fallthrough ",
    "default": "default ",
    "if": "if ",
    "guard": "guard ",
    "else": "else ",
    "for": "for ",
    "do": "do ",
    "in": "in ",
    "while": "while ",
    "where": "where ",
    "break": "break ",
    "continue": "continue",
    "throw": "throw ",
    "catch": "catch",
    "repeat": "repeat ",
    "defer": "defer ",
    "return": "return ",
    # Expressions and Types
    "nil": "nil",
    "true": "true",
    "false": "false",
    "Any": "Any ",
    "as": "as ",
    "is": "is ",
    "self": "self",
    "cap self": "Self",
    "super": "super",
    "try": "try ",
    "try optional": "try? ",
    "try force": "try! ",
    # Contextual
    "convenience": "convenience ",
    "dynamic": "dynamic",
    "didSet": "didSet ",
    "willSet": "willSet ",
    "set": "set ",
    "get": "get ",
    "mutating": "mutating ",
    "nonmutating": "nonmutating",
    "optional": "optional ",
    "lazy": "lazy ",
    "none": "none ",
    "override": "override ",
    "required": "required ",
    "some": "some ",
    "unowned": "unowned ",
    "weak": "weak "
}

ctx.lists["user.code_type"] = {
    "boolean": "Bool",
    "integer": "Int",
    "string": "String",
    "float": "Float",
    "c g float": "CGFloat",
    "any object": "AnyObject",
    "array": "[",
    "dict": "Dictionary<",
    "set": "Set",
}

ctx.lists["user.code_common_function"] = {
    "print": "print",
    "map": "map",
    "flatMap": "flatMap",
    "compactMap": "compactMap",
    "reduce": "reduce",
    "first": "first",
    "last": "last",
    "prefix": "prefix",
    "suffix": "suffix",
    "contains": "contains"
}

@mod.action_class
class UserActions:
    def class_implementing(text: str):
        """Adds protocol conformance to a newly-created class"""

@ctx.action_class("user")
class UserActions:
    def code_operator_lambda():
        actions.user.insert_between("lambda ", ": ")

    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ^ ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" && ")

    def code_operator_or():
        actions.auto_insert(" || ")

    def code_operator_in():
        actions.auto_insert(" in ")

    def code_operator_not_in():
        actions.auto_insert(" in ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_self():
        actions.auto_insert("self")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_insert_null():
        actions.auto_insert("nil")

    def code_insert_is_null():
        actions.auto_insert(" == nil")

    def code_insert_is_not_null():
        actions.auto_insert(" != nil")

    def code_state_if():
        actions.user.insert_between("if ", " {}")

    def code_state_else_if():
        actions.user.insert_between("else if ", " {}")

    def code_state_else():
        actions.insert("else {}")
        actions.key("left enter")

    def code_state_switch():
        actions.user.insert_between("switch ", "{}")

    def code_state_case():
        actions.user.insert_between("case ", ":")

    def code_state_for():
        actions.auto_insert("for ")

    def code_state_for_each():
        actions.user.insert_between("for ", " in ")

    def code_state_while():
        actions.user.insert_between("while ", "{}")

    def code_define_class():
        actions.user.insert_between("class ", "{}")

    def code_define_named_class(text):
        result = "class {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_class_formatter")
            )
        )
        result += " {\n\n}"
        actions.user.paste(result)
        actions.edit.up()
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()

    def class_implementing(text):
        result = ": {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_class_formatter")
            )
        )
        actions.user.paste(result)

    def code_import():
        actions.auto_insert("import ")

    def code_comment_line_prefix():
        actions.auto_insert("// ")

    def code_state_return():
        actions.insert("return ")

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    def code_comment_documentation():
        actions.user.insert_between('/**', '**/')

    def code_insert_function(text: str, selection: str):
        text = func + text + f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        """Inserts private function declaration"""
        result = "func {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private func {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )
        result += " {}"

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()

    def code_protected_function(text: str):
        """Inserts private function declaration"""
        result = "internal func {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )
        result += " {}"

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "public func {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        result += " {}"
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")
