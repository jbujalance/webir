class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class NotSupportedChannelError(Error):
    """
    Exception raised when a not supported TV channel name is sent to the WebIR instance.
    """
    def __init__(self, channel_name, message):
        self.channel = channel_name
        self.message = message

    def __str__(self):
        return self.message
