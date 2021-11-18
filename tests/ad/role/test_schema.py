'''
Testing the users schemas
'''
import pytest
from marshmallow import ValidationError
from tenable.ad.role.schema import RoleSchema, RolePermissionsSchema


@pytest.fixture()
def role_schema_many():
    return [{
        'name': 'name',
        'description': 'description'
    }]


def test_role_schema_many(role_schema_many):
    '''
    Test the role schema with create payload inputs
    '''
    test_resp = [{
        'id': 1,
        'name': 'name',
        'description': 'description',
        'permissions': [{
            'entityName': 'entity_name',
            'action': 'action',
            'entityIds': [1, 2],
            'dynamicId': 'some dynamic id'
        }]
    }]

    schema = RoleSchema()
    assert test_resp[0]['name'] == schema.dump(role_schema_many, many=True)[0]['name']
    assert test_resp[0]['description'] == schema.dump(role_schema_many, many=True)[0]['description']

    with pytest.raises(ValidationError):
        role_schema_many[0]['some_val'] = 'something'
        schema.load(role_schema_many, many=True)


@pytest.fixture()
def role_schema():
    return {
        'name': 'name',
        'description': 'description'
    }


def test_role_schema(role_schema):
    '''
    Test the role schema with create payload inputs
    '''
    test_resp = {
        'id': 1,
        'name': 'name',
        'description': 'description',
        'permissions': [{
            'entityName': 'entity_name',
            'action': 'action',
            'entityIds': [1, 2],
            'dynamicId': 'some dynamic id'
        }]
    }

    schema = RoleSchema()
    assert test_resp['name'] == schema.dump(role_schema)['name']
    assert test_resp['description'] == schema.dump(role_schema)['description']

    with pytest.raises(ValidationError):
        role_schema['some_val'] = 'something'
        schema.load(role_schema)


@pytest.fixture()
def role_permission_schema():
    return {
        'entityName': 'entity_name',
        'action': 'action',
        'entityIds': [1, 2],
        'dynamicId': 'some dynamic id'
    }


def test_role_permission_schema(role_permission_schema):
    '''
    Test the role permission schema. permissions are not passed in any of roles api input,
    exclusively testing with dummy payload just for schema testing
    '''
    test_resp = {
        'entityName': 'entity_name',
        'action': 'action',
        'entityIds': [1, 2],
        'dynamicId': 'some dynamic id'
    }

    schema = RolePermissionsSchema()
    req = schema.dump(schema.load(role_permission_schema))
    assert test_resp['entityName'] == req['entityName']
    assert test_resp['action'] == req['action']
    assert test_resp['entityIds'] == req['entityIds']
    assert test_resp['dynamicId'] == req['dynamicId']

    with pytest.raises(ValidationError):
        role_permission_schema['some_val'] = 'something'
        schema.load(role_permission_schema)


@pytest.fixture()
def role_schema_with_dummy_payload():
    return {
        'name': 'name',
        'description': 'description',
        'permissions': [{
            'entityName': 'entity_name',
            'action': 'action',
            'entityIds': [1, 2],
            'dynamicId': 'some dynamic id'
        }]
    }


def test_role_schema_with_dummy_payload(role_schema_with_dummy_payload):
    '''
    Test the role schema. testing entire response by providing dummy payload
    '''
    test_resp = {
        'id': 1,
        'name': 'name',
        'description': 'description',
        'permissions': [{
            'entityName': 'entity_name',
            'action': 'action',
            'entityIds': [1, 2],
            'dynamicId': 'some dynamic id'
        }]
    }

    schema = RoleSchema()
    req = schema.dump(schema.load(role_schema_with_dummy_payload))
    assert test_resp['name'] == req['name']
    assert test_resp['description'] == req['description']
    assert test_resp['permissions'][0]['entityName'] == req['permissions'][0]['entityName']
    assert test_resp['permissions'][0]['action'] == req['permissions'][0]['action']
    assert test_resp['permissions'][0]['entityIds'] == req['permissions'][0]['entityIds']
    assert test_resp['permissions'][0]['dynamicId'] == req['permissions'][0]['dynamicId']

    with pytest.raises(ValidationError):
        role_schema_with_dummy_payload['some_val'] = 'something'
        schema.load(role_schema_with_dummy_payload)
