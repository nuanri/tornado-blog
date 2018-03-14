from handler import BaseHandler
# from model.auth import User
# from form.auth import RegisterForm, LoginForm
# from utils.enc import encrypt_password


class IndexHandler(BaseHandler):

    def get(self):
        self.render('index.html')
