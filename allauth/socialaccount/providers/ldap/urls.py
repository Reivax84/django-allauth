from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import LDAPOAuth2Provider


urlpatterns = default_urlpatterns(LDAPOAuth2Provider)
