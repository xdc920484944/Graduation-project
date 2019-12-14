from flask import request, render_template, redirect

from app.analyze.draw import Draw
from app.analyze.easy_analyze import Easy_Analyze
from app.controller.use_mysql import find_mysql, insert_mysql, find_mysql_in_city, insert_mysql_in_city
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

        def get_city_code(city):
            # 城市代码查询
            city_code = find_mysql_in_city(city)
            return city_code

        if web == '51job':

            # 数据查询
            data = find_mysql(web=web, occupation=occupation, city=city)
            #数据库中查询不到数据则爬取数据
            if data == []:
                city_code = get_city_code(city)
                if city_code == []:
                    raise NameError('城市编号为空。错误原因:城市不存在或数据库中无数据')
                print('无忧网数据爬取中.....')
                data = get_data_wuyou(occupation=occupation, city=city, city_code=city_code)
                insert_mysql(web=web, data=data)
                global result
                result = data
            #数据库中存在数据则整理数据
            else:
                print('调用数据库中的数据中....')
                result = {occupation: []}
                for d in range(len(data)):
                    result[occupation].append([data[d].occupation, data[d].company_name,
                                               data[d].address, data[d].salary, data[d].release_time, data[d].occ_href,
                                               data[d].com_href, data[d].city])
            result = Easy_Analyze(result).result
            print('分析结果:', result)

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

        return redirect('index')

    return render_template('home.html', form=request.form)


@web.route('/index')
def show():
    # result={'职业': '', '城市': [''], '总数': 0, '已处理数:': 0, '未处理数:': 0, '工资': {}}
    keys = list(result.keys())
    values = list(result.values())

    def bar(keys, values):
        '''
        绘制柱状图前的数据整理
        :param keys: result的所有key
        :param values: result的所有value
        :return:return {'x': x坐标, 'y': y坐标, 'num': 数据条数, 'title': 图像标题, 'xlabel': x轴标题, 'ylabel': y轴标题}
        '''
        title = str(keys[0]) + ':' + str(values[0]) + '     ' + str(keys[1]) + ':' + str(values[1])
        data_num = '数据条数:' + str(values[3])
        x = list(values[5].keys())
        y = list(values[5].values())
        xlabel = '工资级'
        ylabel = '数量'
        return {'x': x, 'y': y, 'num': data_num, 'title': title, 'xlabel': xlabel, 'ylabel': ylabel}

    bar_dict = bar(keys=keys, values=values)
    img_path = Draw(bar_dict=bar_dict).draw_bar()
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
