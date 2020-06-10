from django.shortcuts import render
from elasticsearch import Elasticsearch
# Create your views here.
# es = Elasticsearch(["119.3.84.213"],http_auth=("elastic", "elastic"),port=9200)
# query = es.search(index="zjt_data", body={"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}})