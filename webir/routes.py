from typing import List

from flask import Blueprint, request, current_app, jsonify

from .exceptions import NotSupportedChannelError
from .services import LircRemoteService, ChannelService

remote_blueprint = Blueprint('remote', __name__, url_prefix='/remote')
lirc_remote = LircRemoteService(remote=current_app.config[LircRemoteService.REMOTE_NAME_CONF_KEY])
channel_service = ChannelService()


@remote_blueprint.route('/send/integer/<int:number>')
def send_number(number: int):
    lirc_remote.send_number(number)
    return __response(number)


@remote_blueprint.route('/send/codes/<list:codes>')
def send_codes(codes: List[str]):
    # TODO validate format of the query parameter: count should be an integer
    count = request.args.get('count')
    lirc_remote.send_once(codes, count)
    return __response(codes)


@remote_blueprint.route('/send/channel/<channel>')
def send_channel(channel: str):
    number = channel_service.get_channel_number(channel)
    lirc_remote.send_number(number)
    return __response(channel)


@remote_blueprint.errorhandler(NotSupportedChannelError)
def handle_not_supported_channel_error(error):
    return __response(error.message, "error"), 404


def __response(payload, status='success'):
    return jsonify(
        status=status,
        data=payload
    )
