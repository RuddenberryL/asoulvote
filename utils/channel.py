
from cmath import nan
from typing import List
import qqbot
from qqbot.model.channel import Channel
from qqbot.model.token import Token
from qqbot.model.message import Message, MessagesPager, TypesEnum

class ChannelWrapper:
    def __init__(self, channel_id: str, token: Token) -> None:
        self.channel_id = channel_id
        self.token = token
        self.sandbox_url = 'https://sandbox.api.sgroup.qq.com'
    
    def get_message(self)->List[Message]:
        msg_api = qqbot.MessageAPI(self.token, False)
        pager = MessagesPager("", "", "")
        return msg_api.get_messages(self.channel_id, pager)
    
    def sandbox_get_message(self)->str:
        request_url = '{root_url}/guilds/{guild_id}/channels'.format(root_url = self.sandbox_url, guild_id = guild_id)