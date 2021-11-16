'''
AD Object
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`ADObject <get_api-ad_object>` API endpoints.

Methods available on ``tad.ad_objects``:

.. rst-class:: hide-signature
.. autoclass:: ADObjectAPI

    .. automethod:: details
    .. automethod:: details_by_profile_and_checker
    .. automethod:: details_by_event
    .. automethod:: get_changes
    .. automethod:: search
'''
from typing import List, Dict
from restfly.utils import dict_clean
from tenable.ad.ad_object.schema import ADObjectSchema
from tenable.base.endpoint import APIEndpoint


class ADObjectAPI(APIEndpoint):
    _schema = ADObjectSchema()

    def details(self,
                directory_id: str,
                infrastructure_id: str,
                ad_object_id: str,
                event_id: str) -> Dict:
        '''
        Retrieves the details of a specific AD object.

        Args:
            directory_id:
                The directory instance identifier.
            infrastructure_id:
                The infrastructure instance identifier.
            ad_object_id:
                The AD Object identifier.
            event_id:
                The event identifier.


        Returns:
            dict:
                the AD object.

        Examples:

            >>> tad.ad_object.details(1, 1, 1, 1)
        '''
        return self._schema.load(
            self._api.get(f"infrastructures/{infrastructure_id}/directories/{directory_id}/ad-objects/{ad_object_id}"))

    def details_by_profile_and_checker(self,
                                       profile_id: str,
                                       checker_id: str,
                                       ad_object_id: str) -> Dict:
        '''
        Retrieves an AD object by id that have deviances for a specific profile and checker

        Args:
            profile_id:
                The profile instance identifier.
            checker_id:
                The checker instance identifier.
            ad_object_id:
                The AD Object identifier.


        Returns:
            dict:
                the AD object.

        Examples:

            >>> tad.ad_object.details(1, 1, 1)
        '''
        return self._schema.load(
            self._api.get(f"profiles/{profile_id}/checkers/{checker_id}/ad-objects/{ad_object_id}"))

    def details_by_event(self,
                         directory_id: str,
                         infrastructure_id: str,
                         ad_object_id: str,
                         event_id: str) -> Dict:
        '''
        Retrieves the details of a specific AD object.

        Args:
            directory_id:
                The directory instance identifier.
            infrastructure_id:
                The infrastructure instance identifier.
            ad_object_id:
                The AD Object identifier.
            event_id:
                The event identifier.


        Returns:
            dict:
                the AD object.

        Examples:

            >>> tad.ad_object.details(1, 1, 1, 1)
        '''
        return self._schema.load(
            self._api.get(f"infrastructures/{infrastructure_id}/"
                          f"directories/{directory_id}/"
                          f"events/{event_id}/"
                          f"ad-objects/{ad_object_id}"))

    def get_changes(self,
                    directory_id: str,
                    infrastructure_id: str,
                    ad_object_id: str,
                    event_id: str,
                    **kwargs) -> Dict:
        '''
        Retrieves the details of a specific AD object.

        Args:
            directory_id:
                The directory instance identifier.
            infrastructure_id:
                The infrastructure instance identifier.
            ad_object_id:
                The AD Object identifier.
            event_id:
                The event identifier.
            wanted_values:
                ???


        Returns:
            dict:
                the AD object.

        Examples:

            >>> tad.ad_object.get_changes(1, 1, 1, 1)
        '''
        param = self._schema.dump(self._schema.load(kwargs))
        return self._schema.load(
            self._api.get(f"infrastructures/{infrastructure_id}/"
                          f"directories/{directory_id}/"
                          f"events/{event_id}/"
                          f"ad-objects/{ad_object_id}/changes", params=param),
            many=True)

    def search(self,
               profile_id: str,
               checker_id: str,
               expression: Dict[str, str],
               directories: List[int],
               reasons: List[int],
               show_ignored: bool,
               **kwargs) -> List[Dict]:
        '''
        Search all AD objects having deviances by profile by checker

        Args:
            profile_id:
                The profile instance identifier.
            checker_id:
                The checker instance identifier.
            expression:
                ???
            directories:
                The list of directory instance identifiers.
            reasons:
                The list of reasons identifiers.
            show_ignored:
                ???
            date_start:
                ???
            date_end:
                ???
            page:
                ???
            per_page:
                ???

        Returns:
            dict:
                the AD object.

        Examples:

            >>> tad.ad_object.search() # need to update
        '''
        param = self._schema.dump(self._schema.load(
            dict_clean({
                'page': kwargs.get('page'),
                'perPage': kwargs.get('per_page')
            })
        ))

        payload = self._schema.dump(self._schema.load(
            dict_clean({
                'expressions': expression,
                'directories': directories,
                'reasons': reasons,
                'dateStart': kwargs.get('date_start'),
                'dateEnd': kwargs.get('date_end'),
                'showIgnored': show_ignored
            })
        ))

        return self._schema.load(
            self._api.post(f'profiles/{profile_id}/checkers/{checker_id}/ad-objects/search', params=param, json=payload),
            many=True)
