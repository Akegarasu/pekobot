from typing import Dict, Any, Optional

from .event_adapter import EventAdapter
from .log import logger


class Event(dict):

    @staticmethod
    def from_payload(payload: Dict[str, Any]) -> 'Optional[Event]':
        """
        从事件数据构造 `Event` 对象。
        """
        try:
            e = Event(
                EventAdapter.parse_event(payload)
            )
            logger.debug(e)
            _ = e.event_type, e.detail_type
            return e
        except KeyError:
            return None

    # event_type.detail_type.sub_type
    #   message    group      text
    #   event    deleted_reaction
    @property
    def event_type(self) -> str:
        return self['extra']['type']

    @property
    def detail_type(self) -> str:
        return self['extra'][f'{self.event_type}_type']

    @property
    def sub_type(self) -> Optional[str]:
        return self['extra'].get('sub_type')

    @property
    def name(self):
        n = self.event_type + '.' + self.detail_type
        if self.sub_type:
            n += '.' + self.sub_type
        return n

    # self_id: int  # 机器人自身 ID
    type: int  # 消息类型 文字：1
    event_type: str

    user_id: Optional[str]  # 用户 ID author_id
    author_id: Optional[str]

    group_id: Optional[str]  # 群 ID target_id
    target_id: Optional[str]

    message_id: Optional[str]  # 消息 ID msg_id
    msg_id: Optional[str]

    msg_timestamp: Optional[int]

    message: Optional[Any]  # 消息 content
    content: Optional[Any]

    author: Optional[Dict[str, Any]]  # 消息发送者信息

    def __getattr__(self, key) -> Optional[Any]:
        return self.get(key)

    def __setattr__(self, key, value) -> None:
        self[key] = value

    def __repr__(self) -> str:
        return f'<Event, {super().__repr__()}>'

# pic.group.message
