'''
profiles
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`User <get_api-profile>` API endpoints.

Methods available on ``tad.profiles``:

.. rst-class:: hide-signature
.. autoclass:: ProfilesAPI

    .. automethod:: list
    .. automethod:: create
    .. automethod:: details
    .. automethod:: update
    .. automethod:: delete
    .. automethod:: copy_profile
    .. automethod:: commit
    .. automethod:: unstage
'''
from typing import List, Dict
from tenable.ad.profile.schema import ProfileSchema
from tenable.base.endpoint import APIEndpoint


class UsersAPI(APIEndpoint):
    _path = 'profiles'
    _schema = ProfileSchema()

    def list(self) -> List[Dict]:
        '''
        Retrieve all profiles

        Returns:
            list:
                The list of profile objects

        Examples:

            >>> tad.profiles.list()
        '''
        return self._get()

    def create(self,
               name: str,
               directories: List[int]) -> List[Dict]:
        '''
        Create profile

        Args:
            name:
                The name of new user.
            directories:
                ???


        Return:
            list[dict]:
                The created profile objects

        Example:
            create single user

            >>> tad.profiles.create(
            ...     name='ExampleProfile',
            ...     directories=[1, 2]
            ...     )
        '''
        payload = self._schema.dump({
            'name': name,
            'directories': directories
        })

        return self._schema.load(self._post(json=payload), many=True)

    def details(self,
                profile_id: str) -> Dict:
        '''
        Retrieves the details for a specific profile

        Args:
            profile_id:
                The profile instance identifier.

        Returns:
            dict:
                the profile object.

        Examples:

            >>> tad.profiles.details(1)
        '''
        return self._schema.load(self._get(f'{profile_id}'))

    def update(self,
               profile_id: str,
               **kwargs) -> Dict:
        '''
        update an existing profile

        Args:
            profile_id:
                The profile instance identifier.
            name:
                The name of profile.
            deleted:
                is the profile deleted?
            directories:
                The list of directory ids.


        Returns:
            dict:
                The updated profile object.

        Examples:

            >>> tad.profiles.update(
            ...     profile_id=1,
            ...     name='EDITED'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._patch(f"{profile_id}", json=payload))

    def delete(self, profile_id: str) -> None:
        '''
        delete an existing profile

        Args:
            profile_id:
                The profile instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.profiles.delete(profile_id=1)
        '''
        self._api.delete(f"{profile_id}")

    def copy_profile(self,
                    from_id: str,
                    name: str,
                    directories: List[int]) -> Dict:
        '''
        Creates a new profile from another profile

        Args:
            from_id:
                The profile instance identifier user wants to copy.
            name:
                The name of new profile.
            directories:
                The list of directory ids.


        Returns:
            dict:
                the copied role object.

        Examples:

            >>> tad.profiles.copy_profile(
            ...     from_id=1,
            ...     name='Copied name'
            ...     )
        '''
        payload = self._schema.dump({
            'name': name,
            'directories': directories
        })
        return self._schema.load(self._post(f'from/{from_id}', json=payload))

    def commit(self,
               profile_id: str) -> None:
        '''
        commits change of the related profile

        Args:
            profile_id;
                The profile instance identifier.


        Return:
            None

        Example:
            >>> tad.profiles.commit(1)
        '''
        self._post(f'{profile_id}/commit')

    def unstage(self,
               profile_id: str) -> None:
        '''
        unstages changes of the related profile

        Args:
            profile_id;
                The profile instance identifier.


        Return:
            None

        Example:
            >>> tad.profiles.unstage(1)
        '''
        self._post(f'{profile_id}/unstage')
