from app import creat_app


app = creat_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')

#2019.12.14：分析出来的图片显示错误
