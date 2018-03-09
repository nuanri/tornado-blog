from view import auth

handlers = [
    # (r"/", HomeHandler),
    (r"/register", auth.RegisterHandler),
    (r"/login", auth.LoginHandler)
]
