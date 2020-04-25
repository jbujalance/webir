from flask import Blueprint, request, current_app, jsonify
from .services import LircRemoteService
from typing import List

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


@remote_blueprint.route('/test')
def test():
    return jsonify({'message': 'lol'})
