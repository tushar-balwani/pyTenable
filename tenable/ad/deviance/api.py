'''
deviances
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Deviance <get_api-deviances>` API endpoints.

Methods available on ``tad.deviances``:

.. rst-class:: hide-signature
.. autoclass:: DeviancesAPI

    .. automethod:: list
    .. automethod:: history_details
    .. automethod:: update
    .. automethod:: list_by_directory_and_checker
    .. automethod:: list_by_checker
    .. automethod:: update_by_checker
    .. automethod:: search
    .. automethod:: update_on_ado_and_checker
    .. automethod:: list_by_event
'''
from datetime import datetime
from typing import List, Dict
from restfly.utils import dict_clean
from tenable.ad.deviance.schema import DevianceSchema
from tenable.base.endpoint import APIEndpoint


class DeviancesAPI(APIEndpoint):
    _schema = DevianceSchema()

    def list(self,
             infrastructure_id: str,
             directory_id: str,
             **kwargs) -> List[Dict]:
        '''
        Retrieve all deviances for a directory

        Args:
            infrastructure_id:
                The infrastructure instance identifier.
            directory_id:
                The directory instance identifier.
            page:
                ???
            per_page;
                ???
            batch_size:
                ???
            last_identifier_seen:
                ???
            resolved:
                ???


        Returns:
            list:
                The list of deviance objects

        Examples:

            >>> tad.deviances.list(infrastructure_id='1',
            ...     dashboard_id='1',
            ...     resolved=0
            ...     )
        '''
        param = self._schema.dump(kwargs)
        return self._schema.load(
            self._api.get(f'infrastructures/{infrastructure_id}/directories/{directory_id}/deviances', params=param),
            many=True)

    def history_details(self,
                        infrastructure_id: str,
                        directory_id: str,
                        deviance_id: str) -> Dict:
        '''
        Retrieve ad-object-deviance-history instance by id.


        Args:
            infrastructure_id:
                The infrastructure instance identifier.
            directory_id:
                The directory instance identifier.
            deviance_id:
                The deviance identifier.


        Return:
            dict:
                The deviance object.

        Example:
            >>> tad.deviance.history_details(infrastructure_id='1',
            ...     directory_id='1',
            ...     deviance_id='1'
            ...     )
        '''
        return self._schema.load(
            self._api.get(f'infrastructures/{infrastructure_id}/'
                          f'directories/{directory_id}/'
                          f'deviances/{deviance_id}'))

    def update(self,
               infrastructure_id: str,
               directory_id: str,
               deviance_id: str,
               **kwargs) -> Dict:
        '''
        Retrieve ad-object-deviance-history instance by id.


        Args:
            infrastructure_id:
                The infrastructure instance identifier.
            directory_id:
                The directory instance identifier.
            deviance_id:
                The deviance identifier.
            ignore_until:
                ???


        Return:
            dict:
                The deviance object.

        Example:
            >>> tad.deviance.history_details(infrastructure_id='1',
            ...     directory_id='1',
            ...     deviance_id='1',
            ...     ignore_until=str(datetime.datetime.now())
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._api.patch(
            f'infrastructures/{infrastructure_id}/directories/{directory_id}/deviances/{deviance_id}',
            json=payload))

    def list_by_directory_and_checker(self,
                                      profile_id: str,
                                      infrastructure_id: str,
                                      directory_id: str,
                                      checker_id: str,
                                      **kwargs) -> List[Dict]:
        '''
        Retrieve all deviances related to a single directory and checker

        Args:
            profile_id:
                The profile instance identifier.
            infrastructure_id:
                The infrastructure instance identifier.
            directory_id:
                The directory instance identifier.
            checker_id:
                The checker instance identifier.
            page:
                ???
            per_page;
                ???


        Returns:
            list:
                The list of deviance objects

        Examples:

            >>> tad.deviances.list_by_directory_and_checker(profile_id=1,
            ...     infrastructure_id='1',
            ...     dashboard_id='1',
            ...     checker_id='1'
            ...     page='1'
            ...     )
        '''
        param = self._schema.dump(kwargs)
        return self._schema.load(
            self._api.get(f'profile/{profile_id}/'
                          f'infrastructures/{infrastructure_id}/'
                          f'directories/{directory_id}/'
                          f'checkers/{checker_id}/deviances',
                          params=param),
            many=True)

    def list_by_checker(self,
                        profile_id: str,
                        checker_id: str,
                        **kwargs) -> List[Dict]:
        '''
        Retrieve all deviances for a directory

        Args:
            profile_id:
                The profile instance identifier.
            checker_id:
                The checker instance identifier.
            page:
                ???
            per_page;
                ???
            batch_size:
                ???
            last_identifier_seen:
                ???
            expression:
                ???


        Returns:
            list:
                The list of deviance objects

        Examples:

            >>> tad.deviances.list_by_checker(profile_id='1',
            ...     checker_id='1',
            ...     resolved=0
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(
            self._api.post(f'profiles/{profile_id}/checkers/{checker_id}/deviances', json=payload),
            many=True)

    def update_by_checker(self,
                          profile_id: str,
                          checker_id: str,
                          q_profile_id: str,
                          q_checker_id: str,
                          ignore_until: datetime) -> None:
        '''
        Update instances matching a checker id.

        Args:
            profile_id:
                The profile instance identifier.
            checker_id:
                The checker instance identifier.
            ignore_until:
                ???


        Return:
            None

        Example:
            >>> tad.deviances.update_by_checker(profile_id='1',
            ...     checker_id='1',
            ...     ignore_until=str(datetime.datetime.now())
            ...     )
        '''
        param = self._schema.dump(self._schema.load({
            'profileId': q_profile_id,
            'checkerId': q_checker_id
        }))

        payload = self._schema.dump(self._schema.load({
            'ignoreUntil': ignore_until
        }))

        self._api.patch(f'profiles/{profile_id}/checkers/{checker_id}/deviances', params=param, json=payload)

    def search(self,
               profile_id: str,
               checker_id: str,
               ad_object_id: str,
               **kwargs) -> List[Dict]:
        '''
        Search all deviances by profile by checker by AD object.

        Args:
            per_page:
                ???
            page:
                ???
            date_start:
                ???
            date_end:
                ???
            show_ignored:
                ???


        Return:
            list[dict]:
                The list of deviance objects

        Example:
            >>> tad.deviances.search(profile_id='1',
            ...     checker_id='1',
            ...     ad_object_id='1',
            ...     page='1',
            ...     show_ignored=True
            ...     )
        '''
        param = self._schema.dump(self._schema.load(
            dict_clean({
                'perPage': kwargs.get('per_page'),
                'page': kwargs.get('page')
            })))

        payload = self._schema.dump(self._schema.load(
            dict_clean({
                'dateStart': kwargs.get('date_start'),
                'dateEnd': kwargs.get('date_end'),
                'showIgnored': kwargs.get('show_ignored')
            })
        ))

        return self._schema.load(
            self._api.post(f'profiles/{profile_id}/checkers/{checker_id}/ad-objects/{ad_object_id}', params=param,
                           json=payload),
            many=True)

    def update_on_ado_and_checker(self,
                                  profile_id: str,
                                  checker_id: str,
                                  ad_object_id: str,
                                  q_profile_id: str,
                                  q_checker_id: str,
                                  q_ad_object_id: str,
                                  ignore_until: datetime) -> None:
        '''
        Update the deviances emitted on a specific AD object and for specific checker.


        Args:
            profile_id:
                the profile instance identifier.
            checker_id:
                The checker instance identifier.
            ad_object_id:
                The AD object instance identifier.
            q_profile_id:
                The profile instance identifier for query params.
            q_checker_id:
                The checker instance identifier for query param.
            q_ad_object_id:
                The AD object instance identifier for query param.
            ignore_until:
                ???


        Return;
            None


        Example:
                >>> tad.deviances.update_on_ado_and_checker()
        '''
        param = self._schema.dump(self._schema.load({
            'profileId': q_profile_id,
            'checkerId': q_checker_id,
            'adObjectId': q_ad_object_id
        }))

        payload = self._schema.dump(self._schema.load({
            'ignoreUntil': ignore_until
        }))

        self._api.patch(f'profiles/{profile_id}/checkers/{checker_id}/ad-objects/{ad_object_id}/deviances',
                        params=param, json=payload)

    def list_by_event(self,
                      profile_id: str,
                      infrastructure_id: str,
                      directory_id: str,
                      event_id: str,
                      checkers: List[int],
                      reasons: List[int],
                      **kwargs) -> List[Dict]:
        '''
        Get all deviance by event id

        Args:
            profile_id:
                The profile instance identifier.
            infrastructure_id:
                The infrastructure instance identifier
            directory_id:
                The directory instance identifier.
            event_id:
                The event identifier.
            checkers:
                ???
            reasons:
                ???
            per_page:
                ???
            page:
                ???


        Return:
            list[dict]:
                list of all deviance object

        Example:
            >>> tad.deviances.list_by_event()
        '''
        param = self._schema.dump(self._schema.load(
            dict_clean({
                'page': kwargs.get('page'),
                'perPage': kwargs.get('per_page')
            })
        ))

        payload = self._schema.dump(self._schema.load({
            'checkers': checkers,
            'reasons': reasons
        }))

        return self._schema.load(
            self._api.post(f'profile/{profile_id}/'
                           f'infrastructures/{infrastructure_id}/'
                           f'directories/{directory_id}/'
                           f'events/{event_id}/deviances', params=param, json=payload),
            many=True)
