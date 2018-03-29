import os
import datetime
import random
from validate_email import validate_email

from tornado.web import authenticated

from handler import BaseHandler
from model.auth import User, AuthCode
from form.auth import (
    RegisterForm,
    LoginForm,
    ProfileEditForm,
    ForgetPasswordForm
)
from utils.enc import encrypt_password
from utils.time_ import ftime
from utils.sms import sms
import json


class SmsHandler(BaseHandler):
    def post(self):
        message = {}
        b = self.request.body
        email = json.loads(b).get("email")
        is_valid = validate_email(email)
        if not is_valid:
            message["error"] = "邮箱格式不正确!"
            self.write(json.dumps(message))
            return
        code_type = json.loads(b).get("code_type")
        u_email = self.db.query(User).filter(
            User.email == email
        ).first()
        if str(code_type) == "register":
            if u_email:
                message["error"] = "此邮箱已被注册!"
                self.write(json.dumps(message))
                return
        if str(code_type) == "forget_password":
            if not u_email:
                message["error"] = "无此邮箱!"
                self.write(json.dumps(message))
                return
        code = random.randint(100000, 999999)
        data = {"name": "", "code": code}
        res = sms(email, data)
        print("res ===>", res)
        if res['statusCode'] == 200:
            authcode = AuthCode(
                code=int(code),
                email=email,
                code_type=code_type
            )
            self.db.add(authcode)
            self.db.commit()

            message["success"] = "验证码已发送!"
            self.write(json.dumps(message))


class RegisterHandler(BaseHandler):

    def get(self):
        if self.current_user:
            self.redirect('/')
        form = RegisterForm(self)
        self.render('auth/register.html', form=form)

    def post(self):
        form = RegisterForm(self)
        if form.validate():
            err = {}
            u_username = self.db.query(User).filter(
                User.username == form.username.data
            ).first()
            if u_username:
                err["username"] = ["用户名{}已被占用".format(u_username.username)]
            u_email = self.db.query(User).filter(
                User.email == form.email.data
            ).first()
            if u_email:
                err["emial"] = ["邮箱{}已被占用".format(u_email.email)]
            u_authcode = self.db.query(AuthCode).filter(
                AuthCode.code == form.authcode.data,
                AuthCode.email == form.email.data
            ).first()
            if not u_authcode:
                err["authcode"] = ["验证码不匹配!"]
            if len(err) != 0:
                self.render("auth/register.html", form=form, message=err)
            user = User(username=form.username.data, email=form.email.data)
            user.password = encrypt_password(form.password.data)
            user.img = 'default.jpg'
            user.date_joined = datetime.datetime.now()
            self.db.add(user)
            self.db.delete(u_authcode)
            self.db.commit()
            self.redirect('/login')
        else:
            self.render('auth/register.html', ftime=ftime, form=form, message=form.errors)


class LoginHandler(BaseHandler):

    def get(self):
        if self.current_user:
            self.redirect('/')
        form = RegisterForm(self)
        self.render('auth/login.html', form=form)

    def post(self):
        form = LoginForm(self)
        if form.validate():
            err = {}
            user = self.db.query(User).filter_by(email=form.email.data).first()
            if not user:
                err["username"] = ['用户名密码错误!']
                # self.render('auth/login.html', message=err)
            if not user.validate_password(form.password.data):
                err["username"] = ['用户名密码错误!']
                self.render('auth/login.html', form=form, message=err)
            if user.is_lock:
                err = '无权登陆!'
                self.render('404.html', message=err)
            self.set_secure_cookie("blog_user", str(user.id))
            user.last_login = datetime.datetime.now()
            self.db.commit()
            self.redirect('/')
        else:
            self.render('auth/login.html', ftime=ftime, form=form, message=form.errors)


class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("blog_user")
        self.redirect('/')


class ForgetPasswordHandler(BaseHandler):

    def get(self):
        if self.current_user:
            self.redirect('/')
        form = ForgetPasswordForm(self)
        self.render('auth/forget_password.html', form=form)

    def post(self):
        form = ForgetPasswordForm(self)
        if form.validate():
            err = {}
            get_user = self.db.query(User).filter(
                User.email == form.email.data
            ).first()
            if not get_user:
                err["emial"] = ["无此邮箱{}".format(get_user.email)]
            u_authcode = self.db.query(AuthCode).filter(
                AuthCode.code == form.authcode.data,
                AuthCode.email == form.email.data
            ).first()
            if not u_authcode:
                err["authcode"] = ["验证码不匹配!"]
            if len(err) != 0:
                self.render("auth/forget_password.html", form=form, message=err)
            get_user.password = encrypt_password(form.new_password.data)
            self.db.delete(u_authcode)
            self.db.commit()
            self.redirect('/login')
        else:
            self.render('auth/forget_password.html', ftime=ftime, form=form, message=form.errors)


class ProfileHandler(BaseHandler):

    @authenticated
    def get(self):
        # user = self.db.query(User).filter_by(id=ID).first()
        self.render("auth/profile.html", ftime=ftime)


class ProfileEditHandler(BaseHandler):

    @authenticated
    def get(self):
        form = ProfileEditForm(self)
        form.username.data = self.current_user.username
        form.email.data = self.current_user.email
        form.nickname.data = self.current_user.nickname

        self.render("auth/profile_edit.html", ftime=ftime, form=form)

    @authenticated
    def post(self):
        form = ProfileEditForm(self)
        err = {}
        if form.validate():
            user = self.db.query(User).filter_by(
                id=self.current_user.id
            ).first()
            u_username = self.db.query(User).filter(
                User.id != self.current_user.id,
                User.username == form.username.data
            ).first()
            if u_username:
                err["username"] = ["用户名{}已被占用".format(u_username.username)]
            u_email = self.db.query(User).filter(
                User.id != self.current_user.id,
                User.email == form.email.data
            ).first()
            if u_email:
                err["emial"] = ["邮箱{}已被占用".format(u_email.email)]
            if len(err) != 0:
                self.render("userinfo_edit.html", form=form, message=err)
            user.username = form.username.data
            user.email = form.email.data
            if form.nickname.data:
                user.nickname = form.nickname.data
            self.db.commit()
            self.render("auth/profile.html", ftime=ftime, form=form)
        else:
            self.render("auth/profile_edit.html", form=form, message=form.errors)


class UploadHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render("auth/upload.html")

    @authenticated
    def post(self):
        # print("====>", self.request.files)
        find_file = self.request.files.get('file')
        if find_file is None:
            error = "请选择一张图片！"
            self.render("auth/upload.html", message=error)
        file1 = self.request.files['file'][0]
        original_fname = file1['filename']
        # 分离文件名与扩展名
        extension = os.path.splitext(original_fname)[1]
        # fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        # 重命名文件
        final_filename = self.current_user.email + extension
        output_file = open("static/uploads/" + final_filename, 'wb')
        output_file.write(file1['body'])
        output_file.close
        user = self.db.query(User).filter_by(id=self.current_user.id).first()
        user.img = final_filename
        self.db.commit()
        self.redirect('/auth/profile')
        # self.finish("file" + final_filename + " is uploaded")
        # output_file = open("static/uploads/" + original_fname, 'wb')
        # output_file.write(file1['body'])
        # output_file.close
