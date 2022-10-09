from enums.enums import ActionsEnum as actions
from enums.enums import FieldsEnum as fields
from enums.enums import ModulesEnum as modules
from enums.enums import TagsEnum as tags


class Contracts:
    @staticmethod
    def get_contract_abi(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_contract_source_code(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url