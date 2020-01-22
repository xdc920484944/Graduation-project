# 导入模块
from flask import Flask, request, render_template
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo


# 定义登录表单，并且需要在视图函数（views.py）中实例化

# class RegisterForm:
#     def __init__(self, form):
#         self._form = form
#         self._username = self._form['username']
#         self._email = self._form['email']
#         self._password = self._form['password']
#         self._repassword = self._form['repassword']
#         self.space()
#
#     def username(self):
#         if len(self._username) < 3 and len(self._username) > 20:
#             return ''
#
#     def max_lenth(self,num):
#         pass
#
#     def min_lenth(self,num):
#         pass
#
#     def space(self):
#         values = list(self.form)
#         for v in values:
#             if '' in v:
#                 print('错误:账号、密码、邮箱不能含有空格' )
#                 return '错误:账号、密码、邮箱不能含有空格'
class RegistForm(Form):
    username = StringField(u'用户名', validators=[DataRequired(), Length(3, 10, message=u'请输入3-10位的用户名')])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6, 10)])
    password2 = PasswordField(u'重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(u'注册')