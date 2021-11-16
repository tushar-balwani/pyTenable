'''
attack
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Attack <get_api-attacks>` API endpoints.

Methods available on ``tad.attacks``:

.. rst-class:: hide-signature
.. autoclass:: AttacksAPI

    .. automethod:: list

'''
from typing import List, Dict, Literal
from restfly.utils import dict_merge
from tenable.ad.attack.schema import AttackSchema
from tenable.base.endpoint import APIEndpoint


class AttacksAPI(APIEndpoint):
    _schema = AttackSchema()

    def list(self,
             profile_id: str,
             resource_type: Literal['infrastructure', 'directory', 'hostname', 'ip'],
             resource_value: str,
             **kwargs) -> List[Dict]:
        '''
        Retrieve all attacks

        Args:
            profile_id:
                The attack profile identifier.
            resource_type:
                The type of resource. possible values are ``infrastructure``, ``directory``,
                ``hostname``, ``ip``.
            resource_value:
                The value of resource.
            attack_type_ids:
                The list of attack type ids.
            date_end:
                ???
            date_start:
                ???
            include_closed:
                ???
            limit:
                ???
            order:
                ???
            search:
                ???


        Returns:
            list:
                The list of attacks objects

        Examples:

            >>> tad.attacks.list() # not completed yet
        '''
        params = self._schema.dump(self._schema.load(dict_merge({
            'resourceType': resource_type,
            'resourceValue': resource_value
        }, kwargs)))

        return self._schema.load(self._api.get(f'profiles{profile_id}/attacks', params=params), many=True)
