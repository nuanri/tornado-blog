from tornado.web import url
from view import auth
from view import admin
from view import article
import tornado

handlers = [
    # 登录权限
    url(r"/register", auth.RegisterHandler, name="auth:register"),
    url(r"/login", auth.LoginHandler, name="auth:login"),
    url(r"/logout", auth.LogoutHandler, name="auth:logout"),
    url(r"/auth/profile", auth.ProfileHandler, name="auth:profile"),
    url(r"/auth/profile/edit", auth.ProfileEditHandler, name="auth:profile:edit"),
    url(r"/auth/upload", auth.UploadHandler, name="auth:upload"),
    url(r"/auth/forget_password", auth.ForgetPasswordHandler, name="auth:forget_password"),
    # 发送验证码
    url(r"/auth/sms", auth.SmsHandler, name="auth:sms"),

    # 管理员权限
    url(r"/admin/userlist", admin.UserlistHandler, name="admin:userlist"),
    url(r"/admin/userinfo/([0-9]+)", admin.UserinfoHandler, name="admin:userinfo"),
    url(r"/admin/userinfo/([0-9]+)/edit", admin.UserinfoEditHandler, name="admin:userinfo:edit"),

    url(r"/admin/articlelist", admin.ArticlelistHandler, name="admin:articlelist"),

    # 首页
    url(r"/", article.IndexHandler, name="article:index"),

    # 文章
    url(r"/article/create", article.CreateHandler, name="article:create"),
    url(r"/article/([0-9]+)", article.DetailHandler, name="article:detail"),
    url(r"/article/([0-9]+)/edit", article.EditHandler, name="article:edit"),
    url(r"/article/del/([0-9]+)", article.DeleteHandler, name="article:del"),

    # 无此页面，返回404
    url(r".*", auth.PageNotFoundHandler),
]
