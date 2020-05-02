from typing import List

from flask import Blueprint, request, current_app

from .services import LircRemoteService

remote_blueprint = Blueprint('remote', __name__, url_prefix='/remote')
lirc_remote = LircRemoteService(remote=current_app.config[LircRemoteService.REMOTE_NAME_CONF_KEY])


@remote_blueprint.route('/send/integer/<int:number>')
def send_number(number: int):
    lirc_remote.send_number(number)


@remote_blueprint.route('/send/codes/<list:codes>')
def send_codes(codes: List[str]):
    # TODO validate format of the query parameter: count should be an integer
    count = request.args.get('count')
    lirc_remote.send_once(codes, count)
