class Error(Exception):
    """`pekocore` 所有异常的基类。"""
    pass


class ConnectException(Error):
    def __init__(self, msg):
        self.info = msg

    def __repr__(self):
        return f"<ConnectException, {self.info}>"

    def __str__(self):
        return self.__repr__()


class ApiNotAvailable(Error):
    """ API 不可用。"""
    pass


class ApiError(Error, RuntimeError):
    """调用 开黑啦 API 发生错误。"""
    pass


class HttpFailed(ApiError):
    """HTTP 请求响应码不是 2xx。"""

    def __init__(self, status_code: int):
        self.status_code = status_code
        """HTTP 响应码。"""

    def __repr__(self):
        return f'<HttpFailed, status_code={self.status_code}>'

    def __str__(self):
        return self.__repr__()


class ActionFailed(ApiError):
    """
    开黑啦 已收到 API 请求，但执行失败。
    """

    def __init__(self, result: dict):
        self.info = result

    def __repr__(self):
        return f"<ActionFailed " + ", ".join(
            f"{k}={v}" for k, v in self.info.items()) + ">"

    def __str__(self):
        return self.__repr__()


class NetworkError(Error, IOError):
    """网络错误。"""
    pass


class TimingError(Error):
    """时机错误。"""
    pass
