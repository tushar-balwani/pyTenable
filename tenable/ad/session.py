'''
Tenable.ad session
'''
import warnings
import os

from tenable.base.platform import APIPlatform

from .about import AboutAPI
from .api_keys import APIKeyAPI
from .directories.api import DirectoriesAPI
from .ldap_configuration.api import LDAPConfigurationAPI
from .license.api import LicenseAPI
from .lockout_policy.api import LockoutPolicyAPI
from .preference.api import PreferenceAPI
from .role.api import RolesAPI
from .user.api import UsersAPI
from .widget.api import WidgetsAPI


class TenableAD(APIPlatform):
    _env_base = 'TAD'
    _base_path = 'api'
    _conv_json = True

    def _session_auth(self, **kwargs):
        msg = 'Session Auth isn\'t supported with the Tenable.ad APIs'
        warnings.warn(msg)
        self._log.warning(msg)

    def _key_auth(self, api_key):
        self._session.headers.update({
            'X-API-Key': f'{api_key}'
        })
        self._auth_mech = 'keys'

    def _authenticate(self, **kwargs):
        kwargs['_key_auth_dict'] = kwargs.get('_key_auth_dict', {
            'api_key': kwargs.get('api_key',
                                  os.getenv(f'{self._env_base}_API_KEY')
                                  )
        })
        super()._authenticate(**kwargs)

    @property
    def about(self):
        '''
        The interface object for the
        :doc:`Tenable.ad About APIs <about>`.
        '''
        return AboutAPI(self)

    @property
    def api_keys(self):
        '''
        The interface object for the
        :doc:`Tenable.ad API-Keys APIs <api_keys>`.
        '''
        return APIKeyAPI(self)

    @property
    def directories(self):
        '''
        The interface object for the
        :doc:`Tenable.ad Directories APIs <directories>`.
        '''
        return DirectoriesAPI(self)

    @property
    def ldap_configurations(self):
        return LDAPConfigurationAPI(self)

    @property
    def license(self):
        return LicenseAPI(self)

    @property
    def lockout_policy(self):
        return LockoutPolicyAPI(self)

    @property
    def preferences(self):
        return PreferenceAPI(self)

    @property
    def roles(self):
        return RolesAPI(self)

    @property
    def users(self):
        return UsersAPI(self)

    @property
    def widgets(self):
        return WidgetsAPI(self)
