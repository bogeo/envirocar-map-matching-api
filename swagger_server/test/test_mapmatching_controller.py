# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.track_map_matched import TrackMapMatched  # noqa: E501
from swagger_server.models.track_raw import TrackRaw  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMapmatchingController(BaseTestCase):
    """MapmatchingController integration test stubs"""

    def test_mapmatch_envirocar_track(self):
        """Test case for mapmatch_envirocar_track

        Upload a new raw envirocar track to perform mapmatching
        """
        body = TrackRaw()
        response = self.client.open(
            '/tracks/mapmatching',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
