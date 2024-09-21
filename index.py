import random
from enum import IntEnum

from browser import doc
from browser.html import DIV

random.seed(0)

card_text_pair_dict = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
}


class CardStatus(IntEnum):
    UNFLIPPED = 0
    FLIPPED = 1
    PAIRED = 2


class CardDiv(DIV):

    # 基本樣式: 36x36、圓角、文字置中
    base_class_str = "w-36 h-36 rounded-lg flex items-center justify-center "
    status_to_class_str_dict = {
        # 未翻面樣式: 藍色背景, 滑鼠指標
        CardStatus.UNFLIPPED: base_class_str+"bg-blue-500 cursor-pointer",
        # 翻面樣式: 藍色框線
        CardStatus.FLIPPED: base_class_str+"border-4 border-blue-500",
        # 成對樣式: 綠色背景、白色字體
        CardStatus.PAIRED: base_class_str+"bg-green-500 text-white",
    }

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance.bind("click", instance.on_click)

    def __init__(self, text: str, **kwargs):
        self._text = text
        self.status = CardStatus.UNFLIPPED
        kwargs |= {"Class": self.status_to_class_str_dict[self.status]}
        super().__init__(**kwargs)

    def on_click(self, evt):
        if self.status == CardStatus.UNFLIPPED:
            self.status = CardStatus.FLIPPED
            self.classList = self.status_to_class_str_dict[self.status]
            self.text = self._text
            # self.unbind("click", self.on_click)
        elif self.status == CardStatus.FLIPPED:
            self.status = CardStatus.PAIRED
            self.classList = self.status_to_class_str_dict[self.status]


card_text_list = [
    card_text
    for item in card_text_pair_dict.items()
    for card_text in item
]
random.shuffle(card_text_list)
doc["cards"] <= [
    CardDiv(card_text)
    for card_text in card_text_list
]
