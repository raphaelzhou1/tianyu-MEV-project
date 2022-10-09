from enums.enums import ActionsEnum as actions
from enums.enums import FieldsEnum as fields
from enums.enums import ModulesEnum as modules
from enums.enums import TagsEnum as tags

class Tokens:
    @staticmethod
    def get_total_supply_by_contract_address(contract_address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )
        return url

    @staticmethod
    def get_acc_balance_by_token_and_contract_address(
        contract_address: str, address: str
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url