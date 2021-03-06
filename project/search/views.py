import boto3
import math
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse




def get_video(self,title, *args, **kwargs):
    """[View to show data based on video title]

    Args:
        title ([str]): [Video title]

    Returns:
        [json]: [Data from Dynamodb with Video details]
    """
    title = title
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Video')
    try:
        response = table.get_item(Key={'query': title})
        return JsonResponse({'data':response})
    except Exception as e:
        print(e.response['Error']['Message'])
    return  Response(status=status.HTTP_404_NOT_FOUND)
    
    


def get_video_all(self,request, *args, **kwargs):
    """[View to show all video data from Dynamodb]

    Returns:
        [json]: [All data from DynamoDb ]
    """
    page = int(request.GET.get("page", 1))
    per_page = 9
    dynamodb = boto3.resource('dynamodb')
    data = list()
    table = dynamodb.Table('Video')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    total = len(data)
    start = (page - 1) * per_page
    end = page + per_page
        
    return JsonResponse({
                "data": data[start:end],
                "total": total,
                "page": page,
                "last_page": math.ceil(total / per_page),
            })
