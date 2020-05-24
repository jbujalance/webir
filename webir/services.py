from difflib import SequenceMatcher

from py_irsend import irsend

from .exceptions import NotSupportedChannelError


class LircRemoteService:
    # TODO log the calls with the attributes
    """
    This class acts as an interface to the LIRC daemon that is expected to be installed and running in the host.
    """

    # The configuration key holding the LIRC remote name to be used in this application.
    REMOTE_NAME_CONF_KEY = 'REMOTE_NAME'

    # The prefix of the LIRC 'KEY' namespace
    REMOTE_KEY_PREFIX = 'KEY_'

    def __init__(self, remote: str, lirc_sender=irsend):
        """
        Class constructor.
        :param lirc_sender: The implementation of the LIRC irsend program that is to be used to send IR commands.
        :param remote: The name of the remote that is to be used with irsend.
        """
        self.irsend = lirc_sender
        self.remote = remote

    def list_remotes(self, device=None, address=None):
        # TODO catch the SubprocessError and wrap it on a functional exception meaning the LIRC remote is not available
        self.irsend.list_remotes(device, address)

    def list_codes(self, device=None, address=None):
        self.irsend.list_codes(self.remote, device, address)

    def send_once(self, codes, count=None, device=None, address=None):
        self.irsend.send_once(self.remote, codes, count, device, address)

    def send_number(self, number: int, device=None, address=None):
        digits = list(map(int, str(number)))
        codes = list(map(LircRemoteService.__get_digit_key_code, digits))
        self.send_once(codes, None, device, address)

    @staticmethod
    def __get_digit_key_code(digit: int):
        return LircRemoteService.REMOTE_KEY_PREFIX + str(digit)


class ChannelService:
    """
    This class provides information about the supported channels in this instance of WebIR.
    It mainly provides the channel number given a channel name.
    """

    CHANNELS_CONF_KEY = "CHANNELS"
    MINIMUM_ACCEPTED_RATIO = 0.6

    def __init__(self, channels: dict):
        self.matcher = SequenceMatcher()
        self.channels = channels

    def get_channel_number(self, channel_name: str) -> int:
        best_name, best_number, best_score = self.__get_best_match(channel_name)
        if best_score < ChannelService.MINIMUM_ACCEPTED_RATIO:
            message = f"The channel {channel_name} was matched to {best_name} with a non reliable score of {best_score}"
            raise NotSupportedChannelError(channel_name, message)
        return best_number

    def __get_best_match(self, channel_name: str):
        self.matcher.set_seq2(channel_name)
        best_name, best_number, best_score = None, None, 0
        for (name, number) in self.channels.items():
            self.matcher.set_seq1(name)
            score = self.matcher.ratio()
            if score > best_score:
                best_name, best_number, best_score = name, number, score
        return best_name, best_number, best_score
