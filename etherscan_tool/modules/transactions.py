from enums.enums import ActionsEnum as actions
from enums.enums import FieldsEnum as fields
from enums.enums import ModulesEnum as modules
from enums.enums import TagsEnum as tags

class Transactions:
    @staticmethod
    def get_contract_execution_status(txhash: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_tx_receipt_status(txhash: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_TX_RECEIPT_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url