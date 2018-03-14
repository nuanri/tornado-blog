from handler import BaseHandler
from model.auth import User
from form.auth import RegisterForm, LoginForm
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
            self.db.add(user)
            self.db.commit()
            self.redirect('/login')
        else:
            self.render('register.html', message=form)


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        print("login-->", self.request.arguments)
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

    def get(self):
        # user = self.db.query(User).filter_by(id=ID).first()

        self.render("userinfo.html")


    def post(self):
        pass
