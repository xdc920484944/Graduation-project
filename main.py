from app import creat_app

# 爬虫中的数据格式可以进行优化（去掉最后的搜索工作地点）
# 登入功能
# 后台功能
# 数据库数据插入可以一次性插入
# 数据库回滚功能
# 多线程

app = creat_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='127.0.0.1')
