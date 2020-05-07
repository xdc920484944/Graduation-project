from flask import request, render_template, redirect
from app.analyze.draw import Draw
from app.analyze.easy_analyze import Data_Analyze
from app.controller.home import HOME
from app.controller.register import RegistForm
from app.controller.show import SHOW
from app.web import web


@web.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("======源数据获取======")
        global data, form
        form = dict(request.form)
        print('客户端提交数据:', form)
        data = HOME(form=form).home()
        print('源数据:', len(data[form['key']]), data)
        print("======源数据获取======")
        return redirect('index')
    return render_template('home.html', form=request.form)


@web.route('/index')
def show():
    # 绘制柱状图
    result = Data_Analyze(web=form['web']).sort_salary(data)  # 数据分析
    print('Easy_Analyze:', result)
    his_keys = list(result.keys())
    his_values = list(result.values())
    salary_dict = SHOW.deal_data_of_hist(keys=his_keys, values=his_values)  # 绘图前数据格式处理
    print('salary_dict:', salary_dict)
    img_path = Draw().draw_bar(bar_dict=salary_dict)  # 绘制柱状图

    # 词频分析
    print('========词频分析=========')
    if form['web'] == '51job':
        from app.spider.wuyou.get_content import Get_content
        job_imf, com_imf = Get_content(web=form['web'], data=data)  # 获取职位信息,公司信息
        text_list = list(job_imf.values())  # 职位介绍获取
        texts = ''.join(t[2] for t in text_list)
        # for t in text_list:
        #     texts += t[2]
    elif form['web'] == 'tc':
        from app.spider.tc.get_content import Get_content
        job_imf, com_imf = Get_content(data=data)
        text_list = list(job_imf.values())  # 职位介绍获取
        texts = ''.join(t[7] for t in text_list)
    freq_res = Data_Analyze(web=form['web']).deal_data_freq(texts)  # 职位信息数据处理
    print('词频分析结果:', freq_res)
    freq_img_path = Draw().draw_bar(bar_dict=freq_res)  # 绘制柱状图
    print('职位数据:', job_imf)
    print('公司数据:', com_imf)
    print('freq_img_pat:', freq_img_path)
    print('========词频分析=========')

    return render_template('index.html', keys=his_keys, values=his_values, lenth=len(his_keys), img_path=str(img_path),
                           freq_keys=freq_res['x'], freq_values=freq_res['y'], freq_lenth=len(freq_res['x']),
                           freq_img_path=str(freq_img_path))


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
