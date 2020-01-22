from flask import request, render_template, redirect, flash, get_flashed_messages
from app.analyze.draw import Draw
from app.analyze.easy_analyze import Data_Analyze
from app.controller.home import HOME
from app.controller.register import RegistForm
from app.controller.show import SHOW
from app.web import web


@web.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global data
        form = dict(request.form)
        data = HOME(form=form).home()
        return redirect('index')
    return render_template('home.html', form=request.form)


@web.route('/index')
def show():
    # 绘制柱状图
    result = Data_Analyze().sort_salary(data)  # 数据分析
    print('Easy_Analyze:', result)
    his_keys = list(result.keys())
    his_values = list(result.values())
    bar_dict = SHOW.deal_data_of_hist(keys=his_keys, values=his_values)  # 绘图前数据格式处理
    img_path = Draw(bar_dict=bar_dict).draw_bar()  # 绘制柱状图

    # 词频分析
    texts = SHOW.deal_data_of_freq(data=data)
    freq_res = Data_Analyze().deal_data_freq(texts)

    return render_template('index.html', keys=his_keys, values=his_values, lenth=len(his_keys),
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
    if request.method == "GET":
        return render_template('register.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return u'注册成功'
        else:
            print(form.errors)
            return form.errors
    # return render_template('register.html')
