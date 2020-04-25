from py_irsend import irsend


class LircRemoteService:
    """
    This class acts as an interface to the LIRC daemon that is expected to be installed and running in the host.
    """

    # The configuration key holding the LIRC remote name to be used in this application.
    REMOTE_NAME_CONF_KEY = 'REMOTE_NAME'

    # The prefix of the LIRC 'KEY' namespace
    REMOTE_KEY_PREFIX = 'KEY_'

    def __init__(self, lirc_sender=irsend, remote: str = None):
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
