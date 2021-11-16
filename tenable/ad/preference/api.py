'''
preference
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Preference <get_api-preference>` API endpoints.

Methods available on ``tad.preferences``:

.. rst-class:: hide-signature
.. autoclass:: PreferenceAPI

    .. automethod:: details
    .. automethod:: update
'''
from typing import Dict
from tenable.ad.preference.schema import PreferenceSchema
from tenable.base.endpoint import APIEndpoint


class PreferenceAPI(APIEndpoint):
    _path = 'preferences'
    _schema = PreferenceSchema()

    def details(self) -> Dict:
        '''
        get the user's preferences

        Returns:
            dict:
                The user's preferences object

        Examples:

            >>> tad.preferences.details()
        '''
        return self._get()

    def update(self,
               **kwargs) -> Dict:
        '''
        update the user's preferences

        Args:
            language:
                ???
            preferred_profile_id:
                ???


        Return:
            The user's preferences object

        Example:
            >>> tad.preferences.update() # not completed yet
        '''
        payload = self._schema.dump(self._schema.load(kwargs))
        return self._schema.load(self._patch(json=payload))
