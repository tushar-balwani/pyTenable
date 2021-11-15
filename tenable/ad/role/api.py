'''
roles
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Role <get_api-roles>` API endpoints.

Methods available on ``tad.roles``:

.. rst-class:: hide-signature
.. autoclass:: RolesAPI

    .. automethod:: list
    .. automethod:: create
    .. automethod:: default_roles
    .. automethod:: details
    .. automethod:: update
    .. automethod:: delete
    .. automethod:: copy_role
    .. automethod:: replace_role_permissions
'''
from typing import List, Dict
from tenable.ad.role.schema import RoleSchema
from tenable.base.endpoint import APIEndpoint


class RolesAPI(APIEndpoint):
    _path = 'roles'
    _schema = RoleSchema()

    def list(self) -> List[Dict]:
        '''
        Retrieve all roles

        Returns:
            list:
                The list of roles objects

        Examples:

            >>> tad.roles.list()
        '''
        return self._get()

    def create(self,
               name: str,
               description: int) -> List[Dict]:
        '''
        Create a new widget

        Args:
            name:
                The name of role.
            description:
               The description of role.


        Returns:
            list[dict]:
                The created role object.

        Examples:

            >>> tad.roles.create(
            ...     name='Admin',
            ...     description="all privileges"
            ...     )
        '''
        payload = self._schema.dump({
            'name': name,
            'description': description
        })

        return self._schema.load(self._post(json=payload))

    def default_roles(self) -> List[Dict]:
        '''
        Return the default roles for user creation


        Returns:
            list[dict]:
                The default roles object.

        Examples:

            >>> tad.roles.default_roles()
        '''
        return self._get('user-creation-defaults')

    def details(self, role_id: str) -> Dict:
        '''
        Retrieves the details of a specific role.

        Args:
            role_id:
                The role instance identifier.


        Returns:
            dict:
                the role object.

        Examples:

            >>> tad.roles.details(1)
        '''
        return self._schema.load(self._get(f"{role_id}"))

    def update(self,
               role_id: str,
               **kwargs) -> Dict:
        '''
        update an existing role

        Args:
            role_id:
                The role instance identifier.
            name:
                The name of role.
            description:
               The description of role.


        Returns:
            dict:
                The updated widget object.

        Examples:

            >>> tad.roles.update(
            ...     role_id=1,
            ...     name='Basic'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._api.patch(f"{role_id}", json=payload))

    def delete(self, role_id: str) -> None:
        '''
        delete an existing widget

        Args:
            role_id:
                The role instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.roles.delete(
            ...     role_id=1,
            ...     )
        '''
        self._api.delete(f"{role_id}")

    def copy_role(self,
                  from_id: str,
                  name: str) -> Dict:
        '''
        Creates a new role from another role

        Args:
            from_id:
                The role instance identifier user wants to copy.
            name:
                The name of new role.


        Returns:
            dict:
                the copied role object.

        Examples:

            >>> tad.roles.copy_role(
            ...     from_id=1,
            ...     name='Copied name'
            ...     )
        '''
        payload = self._schema.dump({
            'name': name
        })
        return self._schema.load(self._post(f'from/{from_id}', json=payload))

    def replace_role_permissions(self, role_id: str) -> Dict:
        '''
        Replace permission list for a role

        Args:
            role_id:
                The role instance identifier.


        Returns:
            dict:
                the update permissions role object.

        Examples:

            >>> tad.roles.replace_role_permissions(
            ...     role_id=1,
            ...     )
        '''
        return self._schema.load(self._put(f'{role_id}/permissions'))
