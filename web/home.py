from flask import request, render_template, redirect

from app.analyze.easy_analyze import Easy_Analyze
from app.forms.use_mysql import find_mysql, find_mysql_in_city, insert_mysql
from app.spider.lagou.main import get_data_lagou
from app.spider.wuyou.main import get_data_wuyou
from app.spider.zhilian.main import get_data_zhilian
from app.web import web


@web.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        web = request.form['web']
        occupation = request.form['job']
        city = request.form['city']

        # city_code = find_mysql_in_city(city)  # 城市代码查询
        # if city_code == None:
        #     print('该城市不存在，请重新输入')
        #     return redirect('')
        city_code = 1


        if web == '51job':
            data = find_mysql(web=web, occupation=occupation, city=city)  # 数据查询
            if data == []:
                print('无忧网数据爬取中.....')
                data = get_data_wuyou(occupation=occupation, city=city, city_code=city_code)
                insert_mysql(web=web, data=data)
                result = data
            else:
                print('调用数据库中的数据中....')
                result = {occupation: []}
                for d in range(len(data)):
                    result[occupation].append([data[d].occupation, data[d].company_name,
                               data[d].address, data[d].salary, data[d].release_time, data[d].occ_href,
                               data[d].com_href, data[d].city])
            result = Easy_Analyze(result).result
            print('分析结果:',result)


        if web == 'zhilian':
            data = find_mysql(web=web, occupation=occupation, city=city)
            if data == []:
                print('智联网数据爬取中.....')
                data = get_data_zhilian(occupation=occupation, city=city, city_code=city_code)
                insert_mysql(web=web, data=data)

        if web == 'lagou':
            data = find_mysql(web=web, occupation=occupation, city=city)
            if data == []:
                print('拉钩网数据爬取中.....')
                data = get_data_lagou(occupation=occupation, city=city, city_code=city_code)
                insert_mysql(web=web, data=data)

        return redirect('show')

    return render_template('home.html', form=request.form)


@web.route('/show')
def show():
    return render_template('show.html')


@web.route('/find')
def find():
    return render_template('find.html')


@web.route('/login')
def login():
    form = {'data': 'data'}
    return render_template('login.html', form=form)


@web.route('/register')
def register():
    return render_template('register.html')
