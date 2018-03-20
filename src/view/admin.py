# from tornado.web import authenticated
from handler import BaseHandler, administrator
from model.auth import User
from form.admin import UserinfoEditForm
from utils.time_ import ftime


class UserlistHandler(BaseHandler):

    @administrator
    def get(self):
        users = self.db.query(User).order_by(User.id).all()
        self.render("admin/userlist.html", users=users)


class UserinfoHandler(BaseHandler):

    @administrator
    def get(self, ID):
        user = self.db.query(User).filter_by(id=ID).first()
        if not user:
            self.render('404.html', message="无此用户！")
        self.render("admin/userinfo.html", ftime=ftime, user=user)


class UserinfoEditHandler(BaseHandler):

    @administrator
    def get(self, ID):
        user = self.db.query(User).filter_by(id=ID).first()
        if not user:
            self.render('404.html', message="无此用户！")
        form = UserinfoEditForm(self)
        form.username.data = user.username
        form.email.data = user.email
        form.nickname.data = user.nickname
        form.is_admin.data = user.is_admin
        form.is_lock.data = user.is_lock

        self.render("admin/userinfo_edit.html", ftime=ftime, form=form, user=user)

    @administrator
    def post(self, ID):
        form = UserinfoEditForm(self)
        err = {}
        user = self.db.query(User).filter_by(id=ID).first()
        if not user:
            self.render('404.html', message="无此用户！")
        if form.validate():
            u_username = self.db.query(User).filter(
                User.id != ID,
                User.username == form.username.data
            ).first()
            if u_username:
                err["username"] = ["用户名{}已被占用".format(u_username.username)]
            u_email = self.db.query(User).filter(
                User.id != ID,
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
            user.is_admin = form.is_admin.data
            user.is_lock = form.is_lock.data
            self.db.commit()
            self.render("admin/userinfo.html", ftime=ftime, form=form, user=user)
        else:
            self.render(
                "admin/userinfo_edit.html",
                form=form,
                message=form.errors,
                user=user
            )
