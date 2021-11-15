'''
email_notifiers
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`User <get_api-email-notifiers>` API endpoints.

Methods available on ``tad.email_notifiers``:

.. rst-class:: hide-signature
.. autoclass:: EmailNotifiersAPI

    .. automethod:: list
    .. automethod:: create
    .. automethod:: details
    .. automethod:: update
    .. automethod:: delete
'''
from typing import List, Dict
from tenable.ad.email_notifier.schema import EmailNotifierSchema
from tenable.base.endpoint import APIEndpoint


class EmailNotifiersAPI(APIEndpoint):
    _path = 'email-notifiers'
    _schema = EmailNotifierSchema()

    def list(self) -> List[Dict]:
        '''
        Retrieve all email notifiers instances

        Returns:
            list:
                The list of email notifier objects

        Examples:

            >>> tad.email_notifiers.list()
        '''
        return self._get()

    def create(self,
               **kwargs) -> List[Dict]:
        '''
        Create email notifier instance

        Args:
            OPTION 1:
                input_type:
                    ???
                checkers:
                    ???
                profiles:
                    ???
            OPTION 2:
                attack_types:
                    ???
                profiles:
                    ???


        Return:
            list[dict]:
                The created email notifiers instance objects

        Example:
            create single user

            >>> tad.email_notifiers.create(
            ...     input_type='Deviances',
            ...     checkers=[1, 2],
            ...     profiles=[1, 2]
            ...     )
        '''
        payload = self._schema.dump(self._schema.load(kwargs))
        return self._schema.load(self._post(json=payload))

    def details(self,
                email_notifier_id: str) -> Dict:
        '''
        Retrieves the details for a specific email-notifier

        Args:
            email_notifier_id:
                The email-notifier instance identifier.

        Returns:
            dict:
                the email-notifier object.

        Examples:

            >>> tad.email_notifiers.details(1)
        '''
        return self._schema.load(self._get(f'{email_notifier_id}'))

    def update(self,
               email_notifier_id: str,
               **kwargs) -> Dict:
        '''
        update an existing profile

        Args:
            profile_id:
                The email-notifier instance identifier.
            address:
                ???
            criticity_threshold:
                ???
            directories:
                ???
            description:
                ???
            checkers:
                ???
            attack_types:
                ???
            profiles:
                ???
            input_type:
                ???


        Returns:
            dict:
                The updated email-notifier instance object.

        Examples:

            >>> tad.email_notifiers.update(
            ...     profile_id=1,
            ...     address='EDITED'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._patch(f"{email_notifier_id}", json=payload))

    def delete(self, email_notifier_id: str) -> None:
        '''
        delete an existing profile

        Args:
            email_notifier_id:
                The profile instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.email_notifiers.delete(email_notifier_id=1)
        '''
        self._api.delete(f"{email_notifier_id}")
