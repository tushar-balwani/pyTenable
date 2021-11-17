import datetime
import responses

RE_BASE = 'https://pytenable.tenable.ad/api'


@responses.activate
def test_license_details(api):
    responses.add(responses.GET,
                  f'{RE_BASE}/license',
                  json={
                      'customerName': 'customer name',
                      'maxActiveUserCount': 1,
                      'currentActiveUserCount': 0,
                      'expirationDateUTC': '2021-11-17T13:44:24.259Z',
                      'inAppEula': True,
                      'features': ['something']
                  }
                  )
    resp = api.license.details()
    assert isinstance(resp, dict)
    assert resp['customer_name'] == 'customer name'
    assert resp['max_active_user_count'] == 1
    assert resp['current_active_user_count'] == 0
    assert resp['expiration_date_utc'] == datetime.datetime(2021, 11, 17, 13, 44, 24, 259000,
                                                            tzinfo=datetime.timezone.utc)
    assert resp['in_app_eula'] == True
    assert resp['features'][0] == 'something'


@responses.activate
def test_license_create(api):
    responses.add(responses.POST,
                  f'{RE_BASE}/license',
                  json={
                      'customerName': 'customer name',
                      'maxActiveUserCount': 1,
                      'currentActiveUserCount': 0,
                      'expirationDateUTC': '2021-11-17T13:44:24.259Z',
                      'inAppEula': True,
                      'features': ['something']
                  }
                  )
    resp = api.license.create(ad_license='some license')
    assert isinstance(resp, dict)
    assert resp['customer_name'] == 'customer name'
    assert resp['max_active_user_count'] == 1
    assert resp['current_active_user_count'] == 0
    assert resp['expiration_date_utc'] == datetime.datetime(2021, 11, 17, 13, 44, 24, 259000,
                                                            tzinfo=datetime.timezone.utc)
    assert resp['in_app_eula'] == True
    assert resp['features'][0] == 'something'
