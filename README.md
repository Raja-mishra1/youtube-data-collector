
# youtube-data-collector
youtube-data-collector is Django based web app that collects data using 
YouTube Data API v3 on a particular search query after every 1 min using celery and stores data in AWS Dynamo DB.
The data can be accessed using two endpoints:

       1. http://localhost:1337/api/v1/search_all/ => For all records using pagination
       2. http://localhost:1337/api/v1/search/"query" => For data specific to video title

The application uses celery for task management and Redis as a broker for celery. ​
Initially the app collect data with topic "Corona" , it can be easily modified in core/collec_data.py script and the app would thereby collect the requested data.



## Installation

Since the app uses docker container so it can be easily run with docker

   ​docker-compose up -d --build


##  Scalability

The  application can be scaled  vertically or horizontally and is asynchronous since it uses celery so it can be easily scaled . I have preffered Dynamo Db over Mongo DB since Dynamo DB comes with high security and built in scalability with AWS cloud.

## Architecture

The application uses the following technologies:

    Python: I have prefferd python as a programming language for this application since python being a highly
            dynamic language , encourages rapid development and has a large community and feature rich libraries.

    Django: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
            Used for building rest api endpoints for the search app.
            I have preffered django over flask or any other framework of python since it is highly secure with fast development and real quick MVP's.

    Celery: Celery is an open source asynchronous task queue or job queue which is based on distributed message 
            passing. It is used to run various tasks through django at specified intervals.

    Dynamo DB: Amazon DynamoDB is a fully managed proprietary NoSQL database service that supports key–value and 
             document data structures.

    Youtube Data API V3: The YouTube Data API v3 is an API that provides access to YouTube data, such as videos,
            playlists, and channels.I have used this API to collect information regarding video title, description published date and thumbnail URL of videos on specified topics.


## Architecture diagram

![alt text](https://github.com/Raja-mishra1/youtube-data-collector/blob/master/Architecture_diagram.png)

## Credits

I have taken help from some of the opensource repositories which helped me defining the structure of project.
