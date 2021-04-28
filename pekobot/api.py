import json
import abc
import functools
from aiohttp import ClientSession
from typing import (Dict, Any, Optional, AnyStr, Callable, Union, Awaitable,
                    Coroutine)
from .default_config import API_URL


class Api:
    """
    API 接口类。

    继承此类的具体实现类应实现 `call_action` 方法。
    """

    @abc.abstractmethod
    def call_action(self, action: str, **params) -> Union[Awaitable[Any], Any]:
        """
        调用 API，`action` 为要调用的 API 动作名，`**params`
        为 API 所需参数。

        根据实现类的不同，此函数可能是异步也可能是同步函数。
        """
        pass

    def __getattr__(self,
                    item: str) -> Callable[..., Union[Awaitable[Any], Any]]:
        """获取一个可调用对象，用于调用对应 API。"""
        return functools.partial(self.call_action, item)


async def send_msg(
        content: Optional[str],
        message: Optional[str],
        type: Optional[int],
        channel_id: str,
        group_id: Optional[str],
        token: str,
        compress: Optional[int],
) -> None:
    async with ClientSession() as cs:
        headers = {
            'Authorization': f"Bot {token}",
            'Content-type': 'application/json'
        }
        params = {'compress': compress and 1 or 0}
        data = {
            "type": type or 1,
            "channel_id": channel_id or group_id,
            "content": str(content or message),
        }
        async with cs.post(url=f"{API_URL}/channel/message",
                           data=json.dumps(data),
                           headers=headers,
                           params=params) as rep:
            rep_json = await rep.json()
            return rep_json
