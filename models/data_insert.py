from app.spider.wuyou.get_city import Get_city
from app.models.wuyou import City

city = Get_city()
params = City()



# params = Car(position='职业', conpany_name='公式名字', salary=1000)
# db.session.add(params)
# db.session.commit()