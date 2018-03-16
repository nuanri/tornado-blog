from tornado.web import url
from view import auth
from view import admin
from view import article

handlers = [
    # 登录权限
    url(r"/register", auth.RegisterHandler, name="auth:register"),
    url(r"/login", auth.LoginHandler, name="auth:login"),
    url(r"/logout", auth.LogoutHandler, name="auth:logout"),
    url(r"/profile", auth.ProfileHandler, name="auth:profile"),
    url(r"/profile/edit", auth.ProfileEditHandler, name="auth:profile:edit"),
    url(r"/upload", auth.UploadHandler, name="auth:upload"),

    # 管理员权限
    url(r"/userlist", admin.UserlistHandler, name="admin:userlist"),
    url(r"/userinfo/([0-9]+)", admin.UserinfoHandler, name="admin:userinfo"),
    url(r"/userinfo/([0-9]+)/edit", admin.UserinfoEditHandler, name="admin:userinfo:edit"),

    url(r"/", article.IndexHandler, name="article:index"),
]
