from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag(
    "code_object_oriented",
    desc="Tag for enabling basic object oriented programming commands (objects, classes, etc)",
)

ctx.lists["user.code_function_modifier"] = {
    "public": "public",
    "internal": "internal",
    "private": "private",
    "fileprivate": "fileprivate",
    "final": "final"
}

setting_class_formatter = mod.setting("code_class_formatter", str)

@mod.action_class
class Actions:

    def code_define_named_class(text: str):
        """Starts a class definition, with the given name."""

    def code_class_formatter(name: str):
        """Inserts private function name with formatter"""
        actions.insert(
            actions.user.formatted_text(
                name, settings.get("user.code_private_function_formatter")
            )
        )
