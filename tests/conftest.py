import pytest
import boto3

from moto import mock_dynamodb2
from app.model import TodoDAO


@pytest.fixture
def TodoDAOMock():
    with mock_dynamodb2():
        conn = boto3.resource('dynamodb')
        conn.create_table(
            TableName="Todos",
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id',
                                   'AttributeType': 'N'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1,
                                   'WriteCapacityUnits': 1})
        yield TodoDAO()
