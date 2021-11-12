'''conftest'''
import os

import pytest
from tenable.ad.session import TenableAD


@pytest.fixture(scope='module')
def vcr_config():
    '''vcr config fixture'''
    return {
        'filter_headers': [
            ('X-API-Key', 'accessKey=TAD_API_KEY'),
        ],
    }


@pytest.fixture
def api():
    '''api key fixture'''
    return TenableAD(
        api_keys = os.getenv('TAD_API_KEY', 'ffffffffffffffffffffffffffffffffffff'),
        url='https://pytenable.tenable.ad',
        ssl_verify=False,
        vendor='pytest',
        product='pytenable-automated-testing'
    )
