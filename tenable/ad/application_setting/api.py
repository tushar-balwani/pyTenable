'''
application settings
=============

The following methods allow for interaction into the Tenable.ad
:devportal:`Role <get_api-application-settings>` API endpoints.

Methods available on ``tad.application_settings``:

.. rst-class:: hide-signature
.. autoclass:: ApplicationSettingAPI

    .. automethod:: get_settings
    .. automethod:: update_settings
'''
from typing import Dict
from tenable.ad.application_setting.schema import ApplicationSettingsSchema
from tenable.base.endpoint import APIEndpoint


class ApplicationSettingAPI(APIEndpoint):
    _path = 'application-settings'
    _schema = ApplicationSettingsSchema()

    def get_settings(self) -> Dict:
        '''
        Get the application settings

        Returns:
            dict:
                The application settings objects

        Examples:

            >>> tad.application_settings.get_settings()
        '''
        return self._get()

    def update_settings(self,
                        **kwargs) -> Dict:
        '''
        Update the application settings

        Args:
            user_registration:
                ???
            keep_audit_log:
                ???
            log_retention_period:
                ???
            smtp_server_address:
                ???
            smtp_server_port:
                ???
            smtp_account:
                ???
            smtp_account_password:
                ???
            smtp_user_startTLS:
                ???
            tls:
                ???
            email_sender:
                ???
            default_role_ids:
                ???
            default_profile_id:
                ???
            internal_certificate:
                ???


        Return:
            dict:
                The application settings objects

        Example:
            >>> tad.application_settings.update_settings()
        '''
        payload = self._schema.dump(self._schema.load(kwargs))
        return self._schema.load(self._patch(json=payload))
