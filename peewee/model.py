#coding=utf-8
from peewee import *

#定义一个sqlite的数据库表
db=SqliteDatabase('posts.db')

#Model 是一个数据库模型  一个Model 为一个表
class Post(Model):
	title=CharField(unique=True)
	content=TextField()

	class Meta:
		database=db