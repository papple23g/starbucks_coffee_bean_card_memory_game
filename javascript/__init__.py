from typing import Callable


class JsThis:
    def jsonInit(self, dict: dict):
        return


def this():
    return JsThis()


class JSON:
    def stringify(self, obj: object, replacer: Callable = None, indent: int = None) -> str:
        pass

    def parse(self, str: str) -> object:
        pass
