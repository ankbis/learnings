import boto3

def create_dynamodb_table(table_name, partition_key, sort_key=None):
    """
    Creates a new DynamoDB table with the specified name, partition key, and optional sort key.

    Args:
        table_name (str): The name of the DynamoDB table to create.
        partition_key (str): The name of the partition key for the table.
        sort_key (str, optional): The name of the sort key for the table.

    Returns:
        dict: The description of the created DynamoDB table.
    """
    dynamodb = boto3.resource('dynamodb')

    table_attributes = [{'AttributeName': partition_key, 'AttributeType': 'S'}]
    if sort_key:
        table_attributes.append({'AttributeName': sort_key, 'AttributeType': 'S'})

    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}]
    if sort_key:
        key_schema.append({'AttributeName': sort_key, 'KeyType': 'RANGE'})

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=table_attributes,
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )

    return table.table_description

def test_create_dynamodb_table():
    table_name = 'test_table'
    partition_key = 'id'
    sort_key = 'timestamp'

    table_description = create_dynamodb_table(table_name, partition_key, sort_key)
    assert table_description['TableName'] == table_name
    assert table_description['KeySchema'] == [{'AttributeName': partition_key, 'KeyType': 'HASH'},
                                              {'AttributeName': sort_key, 'KeyType': 'RANGE'}]
    assert table_description['AttributeDefinitions'] == [{'AttributeName': partition_key, 'AttributeType': 'S'},
                                                         {'AttributeName': sort_key, 'AttributeType': 'S'}]
