import logging
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado.options import define, options

from urls import handlers
from database import get_db_session
from settings import SECRET_KEY

define("port", default=8888)


class Application(tornado.web.Application):
    def __init__(self):
        self.db_session = get_db_session()
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret=SECRET_KEY,
            debug=True,
        )

        super(Application, self).__init__(handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    logging.info("torando web server is running")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
