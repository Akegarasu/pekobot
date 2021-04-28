from typing import Dict, Any, Optional


class EventAdapter:
    message_args = {
        1: 'text',
        2: 'image',
        3: 'video',
        4: 'file',
        8: 'voice',
        9: 'kmarkdown'
    }

    @classmethod
    def get_detail_key(cls, arg: int) -> str:
        return cls.message_args[arg]

    @classmethod
    def parse_event(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        if payload['extra']['type'] in cls.message_args:
            key = cls.get_detail_key(payload['extra']['type'])
            payload['extra']['type'] = 'message'

            if payload['channel_type'] == 'PERSON':
                payload['extra']['message_type'] = 'private'
            elif payload['channel_type'] == 'GROUP':
                payload['extra']['message_type'] = 'group'

            payload['extra']['sub_type'] = key

        elif payload['type'] == 255:
            key = payload['extra']['type']
            payload['extra'][f'{key}_type'] = 'system_event'

        return payload
