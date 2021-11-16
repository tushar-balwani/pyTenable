'''
attack type
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Attack Type <get_api-attack_type>` API endpoints.

Methods available on ``tad.attack_types``:

.. rst-class:: hide-signature
.. autoclass:: AttackTypeAPI

    .. automethod:: list

'''
from typing import List, Dict
from tenable.ad.attack_type.schema import AttackTypeSchema
from tenable.base.endpoint import APIEndpoint


class AttackTypeAPI(APIEndpoint):
    _schema = AttackTypeSchema()

    def list(self) -> List[Dict]:
        '''
        Retrieve all attack types

        Returns:
            list:
                The list of attack types objects

        Examples:

            >>> tad.attacks.list_types()
        '''
        return self._schema.load(self._api.get('attack-types'), many=True)
