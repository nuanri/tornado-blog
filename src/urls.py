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
    # 发送验证码
    url(r"/auth/sms", auth.SmsHandler, name="auth:sms"),

    # 管理员权限
    url(r"/userlist", admin.UserlistHandler, name="admin:userlist"),
    url(r"/userinfo/([0-9]+)", admin.UserinfoHandler, name="admin:userinfo"),
    url(r"/userinfo/([0-9]+)/edit", admin.UserinfoEditHandler, name="admin:userinfo:edit"),

    url(r"/articlelist", admin.ArticlelistHandler, name="admin:articlelist"),

    # 首页
    url(r"/", article.IndexHandler, name="article:index"),

    # 文章
    url(r"/article/create", article.CreateHandler, name="article:create"),
    url(r"/article/([0-9]+)", article.DetailHandler, name="article:detail"),
    url(r"/article/([0-9]+)/edit", article.EditHandler, name="article:edit"),
    url(r"/article/del/([0-9]+)", article.DeleteHandler, name="article:del"),
]
