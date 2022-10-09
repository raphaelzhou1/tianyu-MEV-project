from enums.enums import ActionsEnum as actions
from enums.enums import FieldsEnum as fields
from enums.enums import ModulesEnum as modules
from enums.enums import TagsEnum as tags

class GasTracker:
    @staticmethod
    def get_est_confirmation_time(gas_price: int) -> str:
        # NOTE: gas_price in wei, result in seconds
        url = (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ESTIMATE}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
        )
        return url

    @staticmethod
    def get_gas_oracle() -> str:
        # NOTE: gas_price in wei, result in seconds
        url = (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ORACLE}"
        )
        return url