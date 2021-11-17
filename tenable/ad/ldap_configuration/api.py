'''
LDAP configuration
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Role <get_api-ldap-configuration>` API endpoints.

Methods available on ``tad.ldap_configuration``:

.. rst-class:: hide-signature
.. autoclass:: LDAPConfigurationAPI

    .. automethod:: details
    .. automethod:: update
'''
from typing import Dict
from tenable.ad.ldap_configuration.schema import LDAPConfigurationSchema
from tenable.base.endpoint import APIEndpoint


class LDAPConfigurationAPI(APIEndpoint):
    _path = 'ldap-configuration'
    _schema = LDAPConfigurationSchema()

    def details(self) -> Dict:
        '''
        get LDAP configuration singleton

        Returns:
            dict:
                The LDAP configuration object

        Examples:

            >>> tad.ldap_configuration.details()
        '''
        return self._schema.load(self._get())

    def update(self,
               **kwargs) -> Dict:
        '''
        update LDAP configuration singleton

        Args:
            enabled:
                ???
            url:
                ???
            search_user_dn:
                ???
            search_user_password:
                ???
            user_search_base:
                ???
            user_search_filter:
                ???
            allowed_groups:
                name:
                    ???
                default_role_ids:
                    ???
                default_profile_id:
                    ???


        Return:
            The LDAP configuration object

        Example:
            >>> tad.ldap_configuration.update() # not completed yet
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._patch(json=payload))
