import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import LDAPOAuth2Provider


class LDAPOAuth2Adapter(OAuth2Adapter):
    provider_id = LDAPOAuth2Provider.id
    access_token_url = 'https://api.box.com/oauth2/token'
    authorize_url = 'https://account.box.com/api/oauth2/authorize'
    profile_url = 'https://api.box.com/2.0/users/me'
    redirect_uri_protocol = None

    def complete_login(self, request, app, token, **kwargs):
        extra_data = requests.get(self.profile_url, params={
            'access_token': token.token
        })

        # This only here because of weird response from the test suite
        if isinstance(extra_data, list):
            extra_data = extra_data[0]

        return self.get_provider().sociallogin_from_response(
            request,
            extra_data.json()
        )


oauth_login = OAuth2LoginView.adapter_view(LDAPOAuth2Adapter)
oauth_callback = OAuth2CallbackView.adapter_view(LDAPOAuth2Adapter)
