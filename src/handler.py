import mako
# from mako.exceptions import RichTraceback
import mako.lookup

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    lookup = mako.lookup.TemplateLookup(
        ["./templates"], input_encoding='utf-8', output_encoding='utf-8')

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(
            application, request, **kwargs)
        self.template_path = None
        self.title = None
        self.data = {}

    def render_string(self, template_path, **kwargs):
        '''渲染模板，返回字符串
        '''
        if not template_path:
            # 模板未指定，出错
            return 'No template!'

        args = dict(
            handler=self,
            request=self.request,
            current_user=self.current_user,
            static_url=self.static_url,
            xsrf_form_html=self.xsrf_form_html,
            reverse_url=self.reverse_url,
        )

        args.update(self.data)
        args.update(kwargs)

        return self.lookup.get_template(template_path).render(**args)

    def render(self, template_path=None, **kwargs):
        '''渲染模板，直接返回给客户端
        '''

        if not template_path:
            template_path = self.template_path

        html = self.render_string(template_path, **kwargs)

        self.finish(html)

    @property
    def db(self):
        return self.application.db_session()

    def on_finish(self):
        self.application.db_session.remove()

    def get_current_user(self):
        pass
