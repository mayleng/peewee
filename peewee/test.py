#coding=utf-8
from model import *

#通过peewee不用写sql语句就可以直接对数据库进行曾删改差


#连接数据库
db.connect()

#创建表Post
db.create_tables([Post])

#插入数据
Post.create(title='first post ',content='this is first post')
Post.create(title='second post ',content='this is second post')

#查询1条数据---查不到会抛异常
post=Post.get(Post.id==1)
print(post.id)
print(post.title)
print(post.content)

#查询多条数据
posts=Post.select()
for post in posts:
	print(post.id)
	print(post.title)
	print(post.content)

#更新数据
Post.update(title='has been updated ').where(Post.id==1).execute()


#删除一条数据
Post.get(Post.id==1).delete_instance()