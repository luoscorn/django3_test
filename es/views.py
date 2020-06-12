from django.shortcuts import render
from elasticsearch import Elasticsearch
# Create your views here.
# es = Elasticsearch(["119.3.84.213"],http_auth=("elastic", "elastic"),port=9200)
# query = es.search(index="zjt_data", body={"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}})



from drf_haystack.viewsets import HaystackViewSet
from es.models import Book
from es.serializers import BookIndexSerializer
class BookSearchView(HaystackViewSet):
    index_models = [Book]
    serializer_class = BookIndexSerializer
#该视图会返回搜索结果的列表数据，所以如果可以为视图增加REST framework的分页功能。
#我们在配置文件已经定义了分页配置，所以此搜索视图会进行分页