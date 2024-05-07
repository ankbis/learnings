import boto3


def create_dynamodb_table(table_name, partition_key, sort_key=None):
    """
    Creates a new DynamoDB table with the specified configuration.

    Args:
        table_name (str): The name of the DynamoDB table to be created.
        partition_key (str): The name of the partition key for the table.
        sort_key (str, optional): The name of the sort key for the table.

    Returns:
        boto3.resources.factory.dynamodb.Table: The created DynamoDB table object.
    """
    dynamodb = boto3.resource('dynamodb')

    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}]
    if sort_key:
        key_schema.append({'AttributeName': sort_key, 'KeyType': 'RANGE'})

    attribute_definitions = [{'AttributeName': partition_key, 'AttributeType': 'S'}]
    if sort_key:
        attribute_definitions.append({'AttributeName': sort_key, 'AttributeType': 'S'})

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    return table
