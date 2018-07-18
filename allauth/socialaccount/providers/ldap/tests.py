# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import LDAPOAuth2Provider


class LDAPOAuth2Tests(OAuth2TestsMixin, TestCase):
    provider_id = LDAPOAuth2Provider.id

    def get_mocked_response(self):
        return [MockedResponse(200, """{
          "type": "user",
          "id": "123456789",
          "name": "Max Mustermann",
          "login": "balls@johnson.com",
          "created_at": "2017-06-14T09:52:39-08:00",
          "modified_at": "2017-06-14T09:55:11-08:00",
          "language": "fr",
          "timezone": "Europ/Luxembourg",
          "space_amount": 1234,
          "space_used": 0,
          "max_upload_size": 12221,
          "status": "active",
          "job_title": "",
          "phone": "123-333-66664",
          "address": "",
          "avatar_url": ""
        }""")]
