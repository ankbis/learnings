def create_dynamodb_table(table_name, partition_key, sort_key=None):
    """
    Creates a DynamoDB table with the specified name, partition key, and optional sort key.
    
    Args:
        table_name (str): The name of the DynamoDB table to create.
        partition_key (str): The name of the partition key for the table.
        sort_key (str, optional): The name of the sort key for the table.
    
    Returns:
        dict: The response from the DynamoDB client when creating the table.
    """
    import boto3
    
    dynamodb = boto3.resource('dynamodb')
    
    # Define the table attributes
    table_attributes = [
        {
            'AttributeName': partition_key,
            'AttributeType': 'S'
        }
    ]
    
    if sort_key:
        table_attributes.append({
            'AttributeName': sort_key,
            'AttributeType': 'S'
        })
    
    # Create the table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': partition_key,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': sort_key,
                'KeyType': 'RANGE'
            } if sort_key else None
        ],
        AttributeDefinitions=table_attributes,
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    return table.meta.client.describe_table(TableName=table_name)

def test_create_dynamodb_table_with_partition_key():
    table_name = 'test_table'
    partition_key = 'id'
    response = create_dynamodb_table(table_name, partition_key)
    assert response['Table']['TableName'] == table_name
    assert response['Table']['KeySchema'][0]['AttributeName'] == partition_key
    assert response['Table']['AttributeDefinitions'][0]['AttributeName'] == partition_key

def test_create_dynamodb_table_with_partition_and_sort_key():
    table_name = 'test_table'
    partition_key = 'id'
    sort_key = 'timestamp'
    response = create_dynamodb_table(table_name, partition_key, sort_key)
    assert response['Table']['TableName'] == table_name
    assert response['Table']['KeySchema'][0]['AttributeName'] == partition_key
    assert response['Table']['KeySchema'][1]['AttributeName'] == sort_key
    assert response['Table']['AttributeDefinitions'][0]['AttributeName'] == partition_key
    assert response['Table']['AttributeDefinitions'][1]['AttributeName'] == sort_key
