import os

from tornado.web import authenticated

from handler import BaseHandler
from model.auth import User
from form.auth import RegisterForm, LoginForm, UserinfoEditForm
from utils.enc import encrypt_password


class RegisterHandler(BaseHandler):

    def get(self):
        self.render('register.html')

    def post(self):
        print("-->", self.request.arguments)
        form = RegisterForm(self)
        if form.validate():
            user = User(username=form.username.data, email=form.email.data)
            user.password = encrypt_password(form.password.data)
            user.img = 'default.jpg'
            self.db.add(user)
            self.db.commit()
            self.redirect('/login')
        else:
            self.render('register.html', message=form)


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        form = LoginForm(self)
        if form.validate():
            user = self.db.query(User).filter_by(email=form.email.data).first()
            if not user:
                err = '用户名密码错误!'
                self.render('login.html', error=err)
            if not user.validate_password(form.password.data):
                err = '用户名密码错误!'
                self.render('login.html', error=err)
            self.set_secure_cookie("blog_user", str(user.id))
        self.redirect('/')


class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("blog_user")
        self.redirect('/')


class UserinfoHandler(BaseHandler):

    @authenticated
    def get(self):
        # user = self.db.query(User).filter_by(id=ID).first()
        self.render("userinfo.html")


class UserinfoEditHandler(BaseHandler):

    @authenticated
    def get(self):
        form = UserinfoEditForm(self)
        form.username.data = self.current_user.username
        form.email.data = self.current_user.email
        form.nickname.data = self.current_user.nickname

        self.render("userinfo_edit.html", form=form)

    @authenticated
    def post(self):
        form = UserinfoEditForm(self)
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
            self.render("userinfo.html", form=form)
        else:
            self.render("userinfo_edit.html", form=form, message=form.errors)


class UploadHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render("upload.html")

    @authenticated
    def post(self):
        # print("====>", self.request.files)
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
        self.redirect('/userinfo')
        # self.finish("file" + final_filename + " is uploaded")
        # output_file = open("static/uploads/" + original_fname, 'wb')
        # output_file.write(file1['body'])
        # output_file.close
