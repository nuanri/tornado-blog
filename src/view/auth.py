from handler import BaseHandler
from model.auth import User
from form.auth import RegisterForm


class RegisterHandler(BaseHandler):

    def get(self):
        b = 'aaaa'
        self.render('register.html')

    def post(self):
        print("-->", self.request.arguments)
        form = RegisterForm(self)
        if form.validate():
            user = User(username=form.username.data, email=form.email.data)
            self.db.add(user)
            self.db.commit()
            self.redirect('/login')
        # else:
        #     self.render('register.html', form=form)


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html')
