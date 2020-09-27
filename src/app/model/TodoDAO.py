import boto3
from botocore.exceptions import ClientError
from flask import abort


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.table = boto3.resource('dynamodb' , endpoint_url='http://localhost:8001').Table('Todos')
        #

    def get(self, id):
        response = self.table.get_item(Key={'id': id})
        # なぜ存在しないidを指定してもClientErrorにならないのか
        print(response)
        if 'Item' not in response:
            raise abort(404, 'not found')
        return response['Item']

    def get_list(self):
        todo_lst = self.table.scan()
        return todo_lst['Items']

    def create(self, data):
        todo = data
        # incrementしたかったらsequenceテーブル作る
        # 重複しているIDにCreateかけると更新処理になる
        todo['id'] = self.counter = self.counter + 1
        self.table.put_item(Item=todo)
        return todo

    def update(self, id, data):
        response = self.table.update_item(
            Key={
                'id': id,
            },
            UpdateExpression="set task=:task",
            ExpressionAttributeValues={
                ':task': data['task']
            },
            ReturnValues="UPDATED_NEW"
        )
        data['id'] = id
        print(response)
        return data

    def delete(self, id):
        self.table.delete_item(
            Key={
                'id': id
            }
        )
