from pysrc.typing_utils import Block, Workspace

from ..html import DIV

innerWidth = 0
innerHeight = 0


class Blockly:
    Blocks: dict = {}

    @classmethod
    def inject(
        cls,
        elt_id_str: str,
        options_dict: dict,
    ) -> Workspace:
        pass

    class Generator:
        """ 轉譯器
        """
        @classmethod
        def new(cls, name: str) -> 'Blockly.Generator':
            pass

        @classmethod
        def valueToCode(cls, block: Block, name: str, order_int: int) -> str:
            pass

        @classmethod
        def statementToCode(cls, block: Block, name: str) -> str:
            pass

        @classmethod
        def workspaceToCode(workspace: Workspace) -> str:
            pass

    class serialization:
        """ 序列化器
        """
        class blocks:
            class BlockSerializer:
                @classmethod
                def new(cls) -> 'Blockly.serialization.blocks.BlockSerializer':
                    pass

                @classmethod
                def load(
                    cls,
                    blocks_dict: dict,
                    workspace: Workspace,
                ):
                    pass

                @classmethod
                def save(cls, workspace: Workspace) -> object:
                    pass


class console:
    def log(*args, **kwargs):
        pass


def loadImage(*args, **kwargs):
    pass


def requestAnimationFrame(*args, **kwargs):
    pass
