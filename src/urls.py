from tornado.web import url
from view import auth
from view import article

handlers = [
    url(r"/register", auth.RegisterHandler, name="auth:register"),
    url(r"/login", auth.LoginHandler, name="auth:login"),
    url(r"/logout", auth.LogoutHandler, name="auth:logout"),
    url(r"/userinfo", auth.UserinfoHandler, name="auth:userinfo"),
    url(r"/userinfo/edit", auth.UserinfoEditHandler, name="auth:userinfo:edit"),
    url(r"/upload", auth.UploadHandler, name="auth:upload"),

    url(r"/", article.IndexHandler, name="article:index"),
]
