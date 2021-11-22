import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Python getPosts trigger function processed a request.")

    try:
        url = "mongodb://azurecosmosdbln:HEbTAVWb6jit5uNbhFRY9hunPfqWpt2Pu35K2PWFyuhfLYgXmsz1Nd7Dv7pALt7cvytXCjkCvIxiW32Cb5iJ3A==@azurecosmosdbln.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmosdbln@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client["neighborapp-db"]
        collection = database["posts"]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(
            result, mimetype="application/json", charset="utf-8", status_code=200
        )
    except:
        return func.HttpResponse("Bad request.", status_code=400)
