from flask import request, render_template, redirect
from app.analyze.draw import Draw
from app.controller.home import HOME
from app.controller.show import SHOW
from app.web import web


@web.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global result
        form = dict(request.form)
        result = HOME(form=form).home()
        return redirect('index')
    return render_template('home.html', form=request.form)


@web.route('/index')
def show():
    keys = list(result.keys())
    values = list(result.values())
    bar_dict = SHOW.deal_data(keys=keys, values=values)  # 绘图前数据格式处理
    img_path = Draw(bar_dict=bar_dict).draw_bar()  # 绘制柱状图
    return render_template('index.html', keys=keys, values=values, lenth=len(keys),
                           img_path=str(img_path))


@web.route('/find')
def find():
    return render_template('find.html')


@web.route('/login')
def login():
    form = {'data': 'data'}
    return render_template('login.html', form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
    return render_template('register.html')
