import random
from dataclasses import dataclass
from enum import IntEnum

from browser import aio, doc
from browser.html import DIV, IMG, A

random.seed(0)


class GameMode(IntEnum):
    EASY = 0
    """ 簡單模式 """
    HARD = 1
    """ 困難模式 """


GAME_MODE = (
    GameMode.HARD if doc.query.getvalue('hard') == "1" else
    GameMode.EASY
)


@dataclass
class Bean:
    """ 咖啡豆 """
    name: str
    """名稱"""
    baking: str
    """烘培程度: 黃金烘焙、中度烘焙、深度烘焙"""
    origin: list[str]
    """產地"""
    acidity: str
    """酸度: 低、中、高"""
    alcoholity: str
    """醇度: 低、中、高"""
    img_url: str
    """圖片網址"""
    flavor1: str
    """風味1"""
    flavor2: str
    """風味2"""

    @property
    def img_html(self) -> str:
        return f'<img src="{self.img_url}" alt="{self.name}" style="width: 30px; height: auto; border-radius: 8px; position: absolute; top: 80px;" />'

    @property
    def card1_innerhtml(self) -> str:
        """ 卡片1 的內容
        """
        return (
            '<div style="position: relative;">'
            + "<br>".join([
                # 風味1
                f'<span style="font-size: 24px;"><b><u>{self.flavor1}</u></b></span>',
                # 名稱
                f'<span style="font-size: 24px;line-height: 25px;"><b>({self.name})</b></span>',
                # 產區
                f'<span style="font-size: 13px;">{"/".join(self.origin)}</span>',
                # 酸度
                f'<span style="font-size: 13px;">酸度: {self.acidity}</span>',
            ])
            + self.img_html
            + '</div>'
        )

    @property
    def card2_innerhtml(self) -> str:
        """ 卡片2 的內容
        """
        return (
            '<div style="position: relative;">'
            + "<br>".join([
                # 風味2
                f'<span style="font-size: 24px;"><b><u>{self.flavor2}</u></b></span>',
                # 名稱
                f'<span style="font-size: 24px;line-height: 25px;"><b>({self.name})</b></span>',
                # 烘培程度
                f'<span style="font-size: 13px;">{self.baking}</span>',
                # 醇度
                f'<span style="font-size: 13px;">醇度: {self.alcoholity}</span>',
            ])
            # 圖片 (左下角，佔據卡片約1/6)
            + self.img_html
            + '</div>'
        )


EASY_BEAN_LIST = [
    Bean(
        name="輕柳綜合",
        flavor1="焦糖",
        flavor2="檸檬皮",
        baking="黃金烘焙",
        origin=["拉丁美洲", "非洲"],
        acidity="高",
        alcoholity="低",
        img_url="https://i.imgur.com/1Ve9Ext.png",
    ),
    Bean(
        name="派克市場",
        flavor1="可可",
        flavor2="夾心巧克力",
        baking="中度烘焙",
        origin=["拉丁美洲"],
        acidity="中",
        alcoholity="中",
        img_url="https://i.imgur.com/mD14Rf4.png",
    ),
    Bean(
        name="佛羅娜",
        flavor1="黑可可",
        flavor2="焦糖",
        baking="深度烘焙",
        origin=["綜合產區"],
        acidity="低",
        alcoholity="高",
        img_url="https://i.imgur.com/42vwBmG.png",
    ),
    Bean(
        name="閑庭綜合",
        flavor1="烤麥芽",
        flavor2="牛奶巧克力",
        baking="黃金烘焙",
        origin=["拉丁美洲"],
        acidity="中",
        alcoholity="低",
        img_url="https://i.imgur.com/IabYIRs.png",
    ),
    Bean(
        name="家常綜合",
        flavor1="太妃糖",
        flavor2="可可",
        baking="中度烘焙",
        origin=["拉丁美洲"],
        acidity="中",
        alcoholity="中",
        img_url="https://i.imgur.com/qgWmOjv.png",
    ),
    Bean(
        name="濃縮咖啡",
        flavor1="糖蜜",
        flavor2="焦糖烘烤甜味",
        baking="深度烘焙",
        origin=["拉丁美洲", "非洲<br>", "亞洲太平洋"],
        acidity="中",
        alcoholity="高",
        img_url="https://i.imgur.com/8q6Y6hQ.png",
    ),
    Bean(
        name="蘇門答臘",
        flavor1="濃郁草本香料",
        flavor2="質樸辛香料",
        baking="深度烘焙",
        origin=["亞洲太平洋-單一產區·印尼"],
        acidity="低",
        alcoholity="高",
        img_url="https://i.imgur.com/ojGyF8z.png",
    ),
    Bean(
        name="瓜地馬拉",
        flavor1="可可",
        flavor2="烘培香料",
        baking="中度烘焙",
        origin=["拉丁美洲-單一產區瓜地馬拉"],
        acidity="中",
        alcoholity="中",
        img_url="https://i.imgur.com/P5YGIi7.png",
    ),
    Bean(
        name="肯亞",
        flavor1="黑醋栗",
        flavor2="葡萄柚",
        baking="中度烘焙",
        origin=["非洲: 肯亞"],
        acidity="高",
        alcoholity="中",
        img_url="https://i.imgur.com/meYNanR.png",
    ),
    Bean(
        name="哥倫比亞",
        flavor1="烤核桃",
        flavor2="草本香料",
        baking="中度烘焙",
        origin=["拉丁美洲: 哥倫比亞"],
        acidity="中",
        alcoholity="中",
        img_url="https://i.imgur.com/hV3tRmO.png",
    ),
]


HARD_BEAN_LIST = [
    EASY_BEAN_LIST[0],  # 從簡單模式追加一個咖啡豆，用來幫卡牌湊數
    Bean(
        name="尚比亞",
        flavor1="柚子",
        flavor2="甜薑",
        baking="黃金烘焙",
        origin=["非洲"],
        acidity="中到高",
        alcoholity="中",
        img_url="https://i.imgur.com/eiIvdEr.png",
    ),
    Bean(
        name="週年紀念綜合",
        flavor1="雪松",
        flavor2="黑松露",
        baking="深度烘焙",
        origin=["亞洲", "太平洋"],
        acidity="低",
        alcoholity="高",
        img_url="https://i.imgur.com/zERRtQR.png",
    ),
    Bean(
        name="秋季綜合",
        flavor1="雪松",
        flavor2="黑松露",
        baking="深度烘焙",
        origin=["拉丁美洲", "非洲<br>", "亞洲", "太平洋"],
        acidity="中",
        alcoholity="高",
        img_url="https://i.imgur.com/NwBk2Xi.png",
    ),
    Bean(
        name="淺日綜合",
        flavor1="甜石榴",
        flavor2="香草卡士達",
        baking="淺烘焙",
        origin=["印尼蘇門答臘<br>", "哥倫比亞拿里諾"],
        acidity="中偏高",
        alcoholity="中",
        img_url="https://i.imgur.com/LdwuHOT.png",
    ),
    Bean(
        name="深月綜合",
        flavor1="黑胡桃",
        flavor2="松露巧克力",
        baking="深烘焙",
        origin=["印尼蘇門答臘<br>", "哥倫比亞拿里諾"],
        acidity="中偏低",
        alcoholity="中偏高",
        img_url="https://i.imgur.com/YspU8Gw.png",
    ),
]

BEAN_LIST = (
    EASY_BEAN_LIST if GAME_MODE == GameMode.EASY else
    HARD_BEAN_LIST
)

# 預先加載圖片，避免卡牌翻面時圖片閃爍
for bean in BEAN_LIST:
    img: IMG = doc.createElement("img")
    img.src = bean.img_url


card_text_pair_dict = {
    bean.card1_innerhtml: bean.card2_innerhtml
    for bean in BEAN_LIST
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
    base_class_str = "w-36 h-36 rounded-lg items-center justify-center text-center "
    base_color = (
        # 簡單模式: 藍色
        "blue-500" if GAME_MODE == GameMode.EASY else
        # 困難模式: 紫色
        "purple-500"
    )

    status_to_class_str_dict = {
        # 未翻面樣式: 藍色背景, 滑鼠指標
        CardStatus.UNFLIPPED: base_class_str+f"bg-{base_color} cursor-pointer",
        # 翻面樣式: 藍色框線
        CardStatus.FLIPPED: base_class_str+f"border-4 border-{base_color}",
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
        self.innerHTML = self._text

    def to_unflipped(self) -> None:
        self.status = CardStatus.UNFLIPPED
        self.classList = self.status_to_class_str_dict[self.status]
        self.text = ""

    def to_paired(self) -> None:
        self.status = CardStatus.PAIRED
        self.classList = self.status_to_class_str_dict[self.status]
        self.innerHTML = self._text


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

        # # 🐛debug: 翻開所有卡牌並配對 (檢視卡片排版用)
        # for card_div in self.card_div_list:
        #     card_div.to_paired()

    @property
    def card_div_list(self) -> list[CardDiv]:
        return self.div.children

    def _on_click(self, evt) -> None:
        aio.run(self.on_click())

    async def on_click(self) -> None:
        flipped_card_div_list: list[CardDiv] = [
            card_div
            for card_div in self.card_div_list
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
            card_div_list: list[CardDiv] = self.card_div_list
            for card_div in card_div_list:
                card_div.unbind("click", card_div.on_click)
            await aio.sleep(self.cool_down_sec)
            for card_div in card_div_list:
                card_div.bind("click", card_div.on_click)
            a_flipped_card_div.to_unflipped()
            b_flipped_card_div.to_unflipped()
            self.div.bind("click", self._on_click)


table = Table()
doc["table"] <= table.div
doc <= DIV(
    A(">>前往困難版", href="?hard=1", Class="text-blue-500 underline") if GAME_MODE == GameMode.EASY else
    A(">>前往簡單版", href="?hard=0", Class="text-blue-500 underline")
)
