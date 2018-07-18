from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class LDAPOAuth2Account(ProviderAccount):
    pass


class LDAPOAuth2Provider(OAuth2Provider):
    id = 'ldap'
    name = 'LDAP'
    account_class = LDAPOAuth2Account

    def extract_uid(self, data):
        return data['id']

    def extract_common_fields(self, data):
        return dict(name=data.get('display_name'),
                    email=data.get('email'))


provider_classes = [LDAPOAuth2Provider]
