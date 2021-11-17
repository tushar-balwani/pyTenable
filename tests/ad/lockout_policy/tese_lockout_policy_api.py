import responses

RE_BASE = 'https://pytenable.tenable.ad/api'


@responses.activate
def test_lockout_policy_details(api):
    responses.add(responses.GET,
                  f'{RE_BASE}/lockout-policy',
                  json={
                      'enabled': True,
                      'lockoutDuration': 10,
                      'failedAttemptThreshold': 2,
                      'failedAttemptPeriod': 1
                  }
                  )
    resp = api.lockout_policy.details()
    assert isinstance(resp, dict)
    assert resp['enabled'] is True
    assert resp['lockout_duration'] == 10
    assert resp['failed_attempt_threshold'] == 2
    assert resp['failed_attempt_period'] == 1


@responses.activate
def test_lockout_policy_update(api):
    responses.add(responses.PATCH,
                  f'{RE_BASE}/lockout-policy',
                  json=None)
    resp = api.lockout_policy.update()
    assert resp is None


