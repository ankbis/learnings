import unittest
import boto3
from moto import mock_dynamodb2
from dynamodb_utils import create_dynamodb_table


@mock_dynamodb2
class TestCreateDynamoDBTable(unittest.TestCase):

    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb')

    def test_create_table_with_partition_key(self):
        table_name = 'users'
        partition_key = 'user_id'
        create_dynamodb_table(table_name, partition_key)
        table = self.dynamodb.Table(table_name)
        self.assertIsNotNone(table)

    def test_create_table_with_partition_and_sort_key(self):
        table_name = 'orders'
        partition_key = 'order_id'
        sort_key = 'created_at'
        create_dynamodb_table(table_name, partition_key, sort_key)
        table = self.dynamodb.Table(table_name)
        self.assertIsNotNone(table)


if __name__ == '__main__':
    unittest.main()
