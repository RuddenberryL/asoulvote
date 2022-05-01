""" Utiliy functions for guild features of the bot
Author: Ouyang Penzai
Date: 2022-April-3
"""
from typing import List
import qqbot
import requests
from qqbot.model.token import Token
from qqbot.model.guild import Guild
from qqbot.model.channel import Channel


class GuildWrapper:
    """The wrapper of guild utils
    """
    def __init__(self, token: Token) -> None:
        self.token = token
        self.sandbox_url = 'https://sandbox.api.sgroup.qq.com'

    def get_guilds(self) -> List[Guild]:
        """Getting list of guilds which registered for the bot

        Returns:
            List[Guild]: the list of guilds
        """
        api = qqbot.UserAPI(self.token, False)
        guilds = api.me_guilds()
        return guilds

    def get_channels(self, guild_id: str) -> List[Channel]:
        """Getting list of channels by guild id

        Args:
            guild_id (str): _description_

        Returns:
            List[Channel]: _description_
        """
        api = qqbot.ChannelAPI(self.token, False)
        return api.get_channels(guild_id)

    def sandbox_get_channels(self, guild_id: str) -> str:
        request_url = '{root_url}/guilds/{guild_id}/channels'.format(root_url = self.sandbox_url, guild_id = guild_id)
        print(self.token.get_string())
        data = requests.get(request_url, headers={'Authorization': 'Bot {}'.format(self.token.get_string())})
        return data.json()