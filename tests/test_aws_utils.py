import unittest
from unittest.mock import patch

from aws_utils import create_dynamodb_table


class TestCreateDynamoDBTable(unittest.TestCase):

    @patch('boto3.resource')
    def test_create_table_with_partition_key(self, mock_resource):
        table_name = 'test_table'
        partition_key = 'id'
        create_dynamodb_table(table_name, partition_key)
        mock_resource.return_value.create_table.assert_called_with(
            TableName=table_name,
            KeySchema=[{'AttributeName': partition_key, 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': partition_key, 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )

    @patch('boto3.resource')
    def test_create_table_with_partition_and_sort_key(self, mock_resource):
        table_name = 'test_table'
        partition_key = 'id'
        sort_key = 'timestamp'
        create_dynamodb_table(table_name, partition_key, sort_key)
        mock_resource.return_value.create_table.assert_called_with(
            TableName=table_name,
            KeySchema=[{'AttributeName': partition_key, 'KeyType': 'HASH'},
                       {'AttributeName': sort_key, 'KeyType': 'RANGE'}],
            AttributeDefinitions=[{'AttributeName': partition_key, 'AttributeType': 'S'},
                                  {'AttributeName': sort_key, 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )


if __name__ == '__main__':
    unittest.main()
