'''
lockout policy
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Lockout Policy <get_api-lockout-policy>` API endpoints.

Methods available on ``tad.lockout_policy``:

.. rst-class:: hide-signature
.. autoclass:: LockoutPolicyAPI

    .. automethod:: details
    .. automethod:: update
'''
from typing import Dict
from tenable.ad.lockout_policy.schema import LockoutPolicySchema
from tenable.base.endpoint import APIEndpoint


class LDAPConfigurationAPI(APIEndpoint):
    _path = 'lockout-policy'
    _schema = LockoutPolicySchema()

    def details(self) -> Dict:
        '''
        get the lockout policy

        Returns:
            dict:
                The lockout policy object

        Examples:

            >>> tad.lockout_policy.details()
        '''
        return self._get()

    def update(self,
               **kwargs) -> None:
        '''
        update the lockout policy

        Args:
            enabled:
                ???
            lockout_duration:
                ???
            failed_attempt_threshold:
                ???
            failed_attempt_period:
                ???


        Return:
            None

        Example:
            >>> tad.lockout_policy.update() # not completed yet
        '''
        payload = self._schema.dump(self._schema.load(kwargs))
        self._patch(json=payload)
