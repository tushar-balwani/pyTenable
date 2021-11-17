import responses

RE_BASE = 'https://pytenable.tenable.ad/api'


@responses.activate
def test_ldap_configuration_details(api):
    responses.add(responses.GET,
                  f'{RE_BASE}/ldap-configuration',
                  json={
                      'enabled': True,
                      'url': 'test@domain.com',
                      'searchUserDN': 'userDN',
                      'searchUserPassword': 'userPassword',
                      'userSearchBase': 'searchBase',
                      'userSearchFilter': 'searchFilter',
                      'allowedGroups': [{
                          'name': 'group name',
                          'defaultRoleIds': [1, 2],
                          'defaultProfileId': 1
                      }]
                  }
                  )
    resp = api.ldap_configurations.details()
    assert isinstance(resp, dict)
    assert resp['enabled'] is True
    assert resp['url'] == 'test@domain.com'
    assert resp['search_user_dn'] == 'userDN'
    assert resp['search_user_password'] == 'userPassword'
    assert resp['user_search_base'] == 'searchBase'
    assert resp['user_search_filter'] == 'searchFilter'
    assert resp['allowed_groups'][0]['name'] == 'group name'
    assert resp['allowed_groups'][0]['default_role_ids'] == [1, 2]
    assert resp['allowed_groups'][0]['default_profile_id'] == 1


@responses.activate
def test_ldap_configuration_update(api):
    responses.add(responses.PATCH,
                  f'{RE_BASE}/ldap-configuration',
                  json={
                      'enabled': True,
                      'url': 'test@domain.com',
                      'searchUserDN': 'userDN',
                      'searchUserPassword': 'userPassword',
                      'userSearchBase': 'searchBase',
                      'userSearchFilter': 'searchFilter',
                      'allowedGroups': [{
                          'name': 'EDITED',
                          'defaultRoleIds': [1, 2],
                          'defaultProfileId': 1
                      }]
                  }
                  )
    resp = api.ldap_configurations.update(enabled=True,
                                          url='test@domain.com',
                                          search_user_dn='userDN',
                                          search_user_password='userPassword',
                                          user_search_base='searchBase',
                                          user_search_filter='searchFilter',
                                          allowed_groups=[{
                                              'name': 'EDITED',
                                              'default_role_ids': [1, 2],
                                              'default_profile_id': 1
                                          }])
    assert isinstance(resp, dict)
    assert resp['enabled'] is True
    assert resp['url'] == 'test@domain.com'
    assert resp['search_user_dn'] == 'userDN'
    assert resp['search_user_password'] == 'userPassword'
    assert resp['user_search_base'] == 'searchBase'
    assert resp['user_search_filter'] == 'searchFilter'
    assert resp['allowed_groups'][0]['name'] == 'EDITED'
    assert resp['allowed_groups'][0]['default_role_ids'] == [1, 2]
    assert resp['allowed_groups'][0]['default_profile_id'] == 1
