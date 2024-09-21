import random
from enum import IntEnum

from browser import aio, doc
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
    """ 卡牌狀態
    """
    UNFLIPPED = 0
    """未翻面"""
    FLIPPED = 1
    """已翻面"""
    PAIRED = 2
    """已配對"""


class CardDiv(DIV):

    # 基本樣式: 36x36、圓角、文字置中
    base_class_str = "w-36 h-36 rounded-lg flex items-center justify-center "
    status_to_class_str_dict = {
        # 未翻面樣式: 藍色背景, 滑鼠指標
        CardStatus.UNFLIPPED: base_class_str+"bg-blue-500 cursor-pointer",
        # 翻面樣式: 藍色框線
        CardStatus.FLIPPED: base_class_str+"border-4 border-blue-500",
        # 配對樣式: 綠色背景、白色字體
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

    def on_click(self, evt) -> None:
        if self.status == CardStatus.UNFLIPPED:
            self.to_flipped()

    def to_flipped(self) -> None:
        self.status = CardStatus.FLIPPED
        self.classList = self.status_to_class_str_dict[self.status]
        self.text = self._text

    def to_unflipped(self) -> None:
        self.status = CardStatus.UNFLIPPED
        self.classList = self.status_to_class_str_dict[self.status]
        self.text = ""

    def to_paired(self) -> None:
        self.status = CardStatus.PAIRED
        self.classList = self.status_to_class_str_dict[self.status]


class Table:
    """ 牌桌 """
    cool_down_sec = 2

    def __init__(self, **kwargs):
        # 準備卡牌文字列表
        card_text_list = [
            card_text
            for item in card_text_pair_dict.items()
            for card_text in item
        ]
        random.shuffle(card_text_list)

        # 將卡牌置於牌桌上
        self.div = DIV(Class="grid grid-cols-4 gap-4 p-4")
        self.div <= [
            CardDiv(card_text)
            for card_text in card_text_list
        ]
        self.div.bind("click", self._on_click)

    def _on_click(self, evt) -> None:
        aio.run(self.on_click())

    async def on_click(self) -> None:
        flipped_card_div_list: list[CardDiv] = [
            card_div
            for card_div in self.div.children
            if card_div.status == CardStatus.FLIPPED
        ]
        if len(flipped_card_div_list) != 2:
            return
        a_flipped_card_div, b_flipped_card_div = flipped_card_div_list

        # 若配對成功，則將卡牌設為已配對
        if (
            card_text_pair_dict.get(a_flipped_card_div._text) == b_flipped_card_div._text  # noqa
            or card_text_pair_dict.get(b_flipped_card_div._text) == a_flipped_card_div._text  # noqa
        ):
            a_flipped_card_div.to_paired()
            b_flipped_card_div.to_paired()

        # 若配對失敗，則經冷卻時間後將卡牌設翻回
        else:
            self.div.unbind("click", self._on_click)
            card_div_list: list[CardDiv] = self.div.children
            for card_div in card_div_list:
                card_div.unbind("click", card_div.on_click)
            await aio.sleep(self.cool_down_sec)
            for card_div in card_div_list:
                card_div.bind("click", card_div.on_click)
            a_flipped_card_div.to_unflipped()
            b_flipped_card_div.to_unflipped()
            self.div.bind("click", self._on_click)


table = Table()
doc <= table.div
