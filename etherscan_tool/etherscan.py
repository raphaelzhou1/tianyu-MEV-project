import json
from importlib import resources
from json import tool

import requests

from modules import accounts

import configs
from enums.enums import ActionsEnum
 
# from etherscan.utils.parsing import ResponseParser as parser

class Etherscan:
    def __new__(cls, api_key: str, net: str = "MAINNET"):
        with resources.path(configs, f"{net.upper()}.json") as path: # path object
            config_path = str(path) # i.e., /Users/tianyu/Desktop/Blockchain Programs/tianyu-defi-parameters-gathering/etherscan_tool/configs/MAINNET.json
        return cls.from_config(api_key=api_key, config_path=config_path, net=net)

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f: # reads and creates a File Object
            return json.load(f) # converts File to JSON object

    # @staticmethod
    # def __run(func, api_key: str, net: str):
    #     def wrapper(*args, **kwargs):
    #         url = (
    #             f"{fields.PREFIX.format(net.lower()).replace('-main','')}"
    #             f"{func(*args, **kwargs)}"
    #             f"{fields.API_KEY}"
    #             f"{api_key}"
    #         )
    #         r = requests.get(url, headers={"User-Agent": ""})
    #         return parser.parse(r)

    #     return wrapper

    @classmethod
    def from_config(cls, api_key: str, config_path: str, net: str):
        config = cls.__load_config(config_path) # returns JSON object (a dictionary)
        for func, v in config.items(): # each pair in the Dict
            print(func)
            print(v["module"])

            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(accounts, v["module"]), func)
                print(attr)
                setattr(cls, func, cls.__run(attr, api_key, net))
        return cls


# print(Etherscan("TE9HIXVD4MTIGAP9SJB8F3V4E39UTP8C1E"));

def main():
    Etherscan("TE9HIXVD4MTIGAP9SJB8F3V4E39UTP8C1E")

main()