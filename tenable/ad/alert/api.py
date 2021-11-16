'''
alerts
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Alert <get_api-alerts>` API endpoints.

Methods available on ``tad.alert``:

.. rst-class:: hide-signature
.. autoclass:: AlertsAPI

    .. automethod:: list
    .. automethod:: details
    .. automethod:: update
    .. automethod:: update_on_profile
'''
from typing import List, Dict
from tenable.ad.alert.schema import AlertSchema
from tenable.base.endpoint import APIEndpoint


class AlertsAPI(APIEndpoint):
    _path = 'alerts'
    _schema = AlertSchema()

    def list(self,
             profile_id: str,
             **kwargs) -> List[Dict]:
        '''
        Retrieve all alert instances

        Args:
            profile_id:
                The profile instance identifier.
            archived:
                ???
            read:
                ???
            per_page:
                ???
            page:
                ???

        Returns:
            list:
                The list of alerts objects

        Examples:

            >>> tad.alerts.list(
            ...     profile_id=1,
            ...     archived='true'
            ...     read='true'
            ...     )
        '''
        param = self._schema.dump(self._schema.load(kwargs))
        return self._schema.load(self._api.get(f'profile/{profile_id}/alerts', params=param), many=True)

    def details(self,
                alert_id: str) -> Dict:
        '''
        Retrieves the details of a specific alert.

        Args:
            alert_id:
                The alert instance identifier.


        Returns:
            dict:
                the alert object.

        Examples:

            >>> tad.alerts.details(1)
        '''
        return self._schema.load(self._get(f"{alert_id}"))

    def update(self,
               alert_id: str,
               **kwargs) -> Dict:
        '''
        Update alert instance

        Args:
            alert_id:
                The alert instance identifier.
            archived:
                ???
            read:
                ???


        Returns:
            dict:
                The updated alert object.

        Example:
            >>> tad.alerts.update(1,
            ...     archived='true',
            ...     read='true'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._patch(f"{alert_id}", json=payload))

    def update_on_profile(self,
                          profile_id: str,
                          **kwargs) -> Dict:
        '''
        Update alerts for one profile

        Args:
            profile_id:
                The alert instance identifier.
            archived:
                ???
            read:
                ???


        Returns:
            dict:
                The updated alert object.

        Example:
            >>> tad.alerts.update_on_profile(1,
            ...     archived='true',
            ...     read='true'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._api.patch(f"profiles/{profile_id}/alerts", json=payload))
