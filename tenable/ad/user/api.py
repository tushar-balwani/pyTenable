'''
users
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`User <get_api-users>` API endpoints.

Methods available on ``tad.users``:

.. rst-class:: hide-signature
.. autoclass:: UsersAPI

    .. automethod:: list
    .. automethod:: create
    .. automethod:: info
    .. automethod:: details
    .. automethod:: update
    .. automethod:: delete
    .. automethod:: log_in
    .. automethod:: log_out
    .. automethod:: create_password
    .. automethod:: retrieve_password
    .. automethod:: change_password
    .. automethod:: update_user_roles
'''
from typing import List, Dict
from restfly.utils import dict_merge
from tenable.ad.user.schema import UserSchema, UserInfoSchema
from tenable.base.endpoint import APIEndpoint


class UsersAPI(APIEndpoint):
    _path = 'users'
    _schema = UserSchema()

    def list(self) -> List[Dict]:
        '''
        Retrieve all users

        Returns:
            list:
                The list of users objects

        Examples:

            >>> tad.users.list()
        '''
        return self._get()

    def create(self,
               name: str,
               email: str,
               password: str,
               **kwargs) -> List[Dict]:
        '''
        Create users

        Args:
            name:
                The name of new user.
            email:
                The email address of the user.
            password:
                The password for the new user.
            surname:
                The surname of new user.
            department:
                The department of user.
            biography:
                The biography of user.
            active:
                is the user active?
            picture:
                The list of picture numbers


        Return:
            list[dict]:
                The created user objects

        Example:
            create single user

            >>> tad.users.create({
            ...     })
        '''
        payload = self._schema.dump(dict_merge({
            'name': name,
            'email': email,
            'password': password
        }, kwargs))

        return self._schema.load(self._post(json=payload))

    def info(self) -> Dict:
        '''
        gets user information

        Return:
            dict:
                The user info object

        Example:
            >>> tad.users.info()
        '''
        schema = UserInfoSchema()
        return schema.load(self._get(f'whoami'))

    def details(self, user_id: str) -> Dict:
        '''
        Retrieves the details for a specific user

        Args:
            user_id:
                The user instance identifier.

        Returns:
            dict:
                the user object.

        Examples:

            >>> tad.users.details(1)
        '''
        return self._schema.load(self._get(f'{user_id}'))

    def update(self,
               user_id: str,
               **kwargs) -> Dict:
        '''
        update an existing user

        Args:
            user_id:
                The user instance identifier.
            name:
                The name of new user.
            email:
                The email address of the user.
            password:
                The password for the new user.
            surname:
                The surname of new user.
            department:
                The department of user.
            biography:
                The biography of user.
            active:
                is the user active?
            picture:
                The list of picture numbers


        Returns:
            dict:
                The updated user object.

        Examples:

            >>> tad.users.update(
            ...     user_id=1,
            ...     name='EDITED'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._patch(f"{user_id}", json=payload))

    def delete(self, user_id: str) -> None:
        '''
        delete an existing user

        Args:
            user_id:
                The user instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.users.delete(user_id=1)
        '''
        self._api.delete(f"{user_id}")

    def log_in(self, auth_token: str) -> None:
        '''
        Logs in a user

        Args:
            auth_token:
                The user instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.users.log_in(auth_token=???)
        '''
        payload = self._schema.dump(self._schema.load({
            'authToken': auth_token
        }))
        return self._schema.load(self._post(json=payload))

    def log_out(self) -> None:
        '''
        Logs out a user


        Returns:
            None:

        Examples:

            >>> tad.users.log_out()
        '''
        return self._schema.load(self._post())

    def create_password(self, email: str) -> None:
        '''
        Sends an email to create new password

        Args:
            email:
                The email address of the user.


        Returns:
            None:

        Examples:

            >>> tad.users.create_password(email='test@domain.com')
        '''
        payload = self._schema.dump({
            'email': email
        })
        return self._schema.load(self._post(f'forgotten-password', json=payload))

    def retrieve_password(self,
                          token: str,
                          new_password: str) -> None:
        '''
        Retrieves a user password

        Args:
            token:
                user token.
            new_password:
                new password for user.


        Returns:
            None:

        Examples:

            >>> tad.users.retrieve_password(
            ...     token='token',
            ...     new_password='xyz'
            ...     )
        '''
        payload = self._schema.dump(self._schema.dump({
            'token': token,
            'newPassword': new_password
        }))
        return self._schema.load(self._post(f'retrieve-password', json=payload))

    def change_password(self,
                        old_password: str,
                        new_password: str) -> None:
        '''
        update a user password

        Args:
            old_password:
                old password of user.
            new_password:
                new password of user.


        Returns:
            None:

        Examples:

            >>> tad.users.change_password(
            ...     old_password='abc',
            ...     new_password='xyz'
            ...     )
        '''
        payload = self._schema.dump(self._schema.load({
            'oldPassword': old_password,
            'newPassword': new_password
        }))
        return self._schema.load(self._patch("password", json=payload))

    def update_user_roles(self,
                          user_id: str,
                          roles: List[int]) -> Dict:
        '''
        Replace role list for user

        Args:
            user_id:
                The user instance identifier.
            roles:
                The list of user role identifiers.


        Returns:
            dict:
                updated user roles object

        Examples:

            >>> tad.users.update_user_roles(
            ...     user_id='1',
            ...     roles=[1, 2, 3]
            ...     )
        '''
        payload = self._schema.dump({
            'roles': roles
        })
        return self._schema.load(self._put(f'{user_id}/roles', json=payload))
