import connexion
import six

from swagger_server.models.track_map_matched import TrackMapMatched  # noqa: E501
from swagger_server.models.track_raw import TrackRaw  # noqa: E501
from swagger_server import util


def mapmatch_envirocar_track(body):  # noqa: E501
    """Upload a new raw envirocar track to perform mapmatching

    Upload a new raw envirocar track to perform mapmatching # noqa: E501

    :param body: raw envirocar track
    :type body: dict | bytes

    :rtype: TrackMapMatched
    """
    if connexion.request.is_json:
        body = TrackRaw.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
