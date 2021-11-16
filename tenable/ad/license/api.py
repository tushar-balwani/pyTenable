'''
license
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`License <get_api-license>` API endpoints.

Methods available on ``tad.license``:

.. rst-class:: hide-signature
.. autoclass:: LicenseAPI

    .. automethod:: details
    .. automethod:: create
'''
from typing import Dict
from tenable.ad.license.schema import LicenseSchema
from tenable.base.endpoint import APIEndpoint


class LDAPConfigurationAPI(APIEndpoint):
    _path = 'license'
    _schema = LicenseSchema()

    def details(self) -> Dict:
        '''
        get license singleton

        Returns:
            dict:
                The license object

        Examples:

            >>> tad.license.details()
        '''
        return self._get()

    def create(self,
               license: str) -> Dict:
        '''
        create new license singleton

        Args:
            license:
                ???


        Return:
            The license object

        Example:
            >>> tad.ldap_configuration.update() # not completed yet
        '''
        payload = self._schema.dump(self._schema.load({
            'license': license
        }))
        return self._schema.load(self._patch(json=payload))
