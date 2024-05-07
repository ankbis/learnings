import boto3


def create_dynamodb_table(table_name, partition_key, sort_key=None):
    """
    Creates a new DynamoDB table with the specified partition and sort keys.

    Args:
        table_name (str): The name of the DynamoDB table to create.
        partition_key (str): The name of the partition key for the table.
        sort_key (str, optional): The name of the sort key for the table.
    """
    dynamodb = boto3.resource('dynamodb')

    # Define the key schema for the table
    key_schema = [
        {'AttributeName': partition_key, 'KeyType': 'HASH'}
    ]
    if sort_key:
        key_schema.append({'AttributeName': sort_key, 'KeyType': 'RANGE'})

    # Define the attribute definitions for the table
    attribute_definitions = [
        {'AttributeName': partition_key, 'AttributeType': 'S'}
    ]
    if sort_key:
        attribute_definitions.append({'AttributeName': sort_key, 'AttributeType': 'S'})

    # Create the table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait for the table to be created
    table.wait_until_exists()
