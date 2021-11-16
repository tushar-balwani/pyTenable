'''
attack type options
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Attack Type Option <get_api-attack_type_option>` API endpoints.

Methods available on ``tad.attack_type_options``:

.. rst-class:: hide-signature
.. autoclass:: AttackTypeOptionsAPI

    .. automethod:: list
    .. automethod:: create
'''
from typing import List, Dict
from restfly.utils import dict_merge
from tenable.ad.attack_type_option.schema import AttackTypeOptionsSchema
from tenable.base.endpoint import APIEndpoint


class AttackTypeOptionsAPI(APIEndpoint):
    _schema = AttackTypeOptionsSchema()

    def list(self,
             profile_id: str,
             attack_type_id: str,
             **kwargs) -> List[Dict]:
        '''
        get all attack type options related to a profile and attack type.

        Args:
            profile_id:
                The attack profile identifier.
            attack_type_id:
                The attack type identifier.
            staged:
                ???
            per_page:
                ???
            page:
                ???


        Returns:
            list:
                The list of attack type options objects

        Examples:

            >>> tad.attacks.list()
        '''
        schema = AttackTypeOptionsSchema()
        params = schema.dump(schema.load(kwargs))
        return schema.load(self._get(f'{profile_id}/attack-types/{attack_type_id}/attack-type-options',
                                     param=params), many=True)

    def create(self,
               profile_id: str,
               attack_type_id: str,
               codename: str,
               value: str,
               value_type: str,
               **kwargs) -> Dict:
        '''
        Create attack type options related to a profile and attack type.

        Args:
            profile_id:
                The attack profile identifier.
            attack_type_id:
                The attack type identifier.
            codename:
                ???
            value:
                ???
            value_type:
                ???
            directory_id:
                The directory identifier.


        Return:
            The newly created attack type options.

        Example:
            >>> tad.attacks.create(profile_id=1,
            ...     attack_type_id=1,
            ...     codename='Somename',
            ...     value='Some value',
            ...     value_type='float',
            ...     directory_id=1
            ...     )
        '''
        payload = self._schema.dump(self._schema.load(dict_merge({
            'value': value,
            'valueType': value_type,
            'codename': codename,
        }, kwargs)))

        return self._schema.load(
            self._post(f'{profile_id}/attack-types/{attack_type_id}/attack-type-options', json=payload))
