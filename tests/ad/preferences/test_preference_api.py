import responses

RE_BASE = 'https://pytenable.tenable.ad/api'


@responses.activate
def test_preference_details(api):
    responses.add(responses.GET,
                  f'{RE_BASE}/preferences',
                  json={
                      'language': 'some language',
                      'preferredProfileId': 1
                  }
                  )
    resp = api.preferences.details()
    assert isinstance(resp, dict)
    assert resp['language'] == 'some language'
    assert resp['preferred_profile_id'] == 1


@responses.activate
def test_preference_update(api):
    responses.add(responses.PATCH,
                  f'{RE_BASE}/preferences',
                  json={
                      'language': 'some other language',
                      'preferredProfileId': 2
                  })
    resp = api.preferences.update(language='some other language',
                                  preferred_profile_id='2')
    assert isinstance(resp, dict)
    assert resp['language'] == 'some other language'
    assert resp['preferred_profile_id'] == 2
