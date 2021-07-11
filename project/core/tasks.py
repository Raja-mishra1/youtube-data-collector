from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command
from .collect_data import get_video_information
from datetime import datetime
import boto3
import uuid


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    """
    celery task to collect data from youtube and add data to DynamoDB
    """
    options = {"query":"Corona","max_results":150}
    data = get_video_information(options)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Video')
    count = 1
    for title,desc,date,url in zip(data['videos_name'],data['description'],data['publishing_date'],data["thumbnail_url"]):
        table.put_item(
            Item={
                'ID':str(uuid.uuid4()),
                'title': title, 
                'description': desc, 
                'published_date': date,
                'thumbnail': url,
                'query':options['query'],
            }
        )
        count+=1       
            
        logger.info(f'{count} ROW ADDED')

