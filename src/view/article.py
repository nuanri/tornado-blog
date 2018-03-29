import datetime
from sqlalchemy import desc, or_

from form.article import ArticleForm
from handler import BaseHandler, administrator
from model.article import Article
from utils.time_ import ftime
from utils.pagination import get_info, custom_rule


class IndexHandler(BaseHandler):

    def get(self):
        sub_string = self.get_argument("keyword", default=None)
        if sub_string is None:
            a = self.db.query(Article).filter_by(
                is_public=True
            ).order_by(desc(Article.id))
        else:
            a = self.db.query(Article).filter(
                or_(
                    # ilike 可以忽略大小写查询
                    Article.title.ilike('%{}%'.format(sub_string)),
                    Article.content.ilike('%{}%'.format(sub_string)))
                ).order_by(desc(Article.id))

        cur_page, page_size, start, stop = get_info(self)
        total = a.count()
        articles = a.slice(start, stop)

        path_url = self.request.uri
        d = custom_rule(cur_page, total, page_size, path_url)
        self.render('index.html', ftime=ftime, articles=articles, d=d)


class CreateHandler(BaseHandler):

    @administrator
    def get(self):
        self.render('article/create.html')

    @administrator
    def post(self):
        form = ArticleForm(self)
        if form.validate():
            article = Article(
                user=self.current_user,
                title=form.title.data,
                content=form.content.data
            )
            article.is_public = form.is_public.data
            self.db.add(article)
            self.db.commit()
            self.redirect('/')
        else:
            self.render("article/create.html", message=form.errors)


class DetailHandler(BaseHandler):

    def get(self, ID):

        article = self.db.query(Article).filter_by(id=ID).first()
        if not article:
            self.render('404.html', message="无此文章！")
        else:
            self.render("article/detail.html", ftime=ftime, article=article)


class EditHandler(BaseHandler):

    @administrator
    def get(self, ID):
        form = ArticleForm(self)

        article = self.db.query(Article).get(ID)
        if article.user != self.current_user:
            self.render('404.html', message="无此权限！")
            return
        article = self.db.query(Article).filter_by(id=ID).first()
        if not article:
            self.render('404.html', message="无此文章！")
            return
        form.title.data = article.title
        form.content.data = article.content
        form.is_public.data = article.is_public

        self.render("article/edit.html", form=form)

    @administrator
    def post(self, ID):
        form = ArticleForm(self)
        if form.validate():
            article = self.db.query(Article).filter_by(id=ID).one()
            article.title = form.title.data
            article.content = form.content.data
            article.is_public = form.is_public.data
            article.updated = datetime.datetime.now()
            self.db.commit()
            self.render("article/detail.html", ftime=ftime, article=article)
        else:
            self.render("article/edit.html", form=form, message=form.errors)


class DeleteHandler(BaseHandler):

    @administrator
    def get(self, ID):

        article = self.db.query(Article).filter_by(id=ID).first()
        if not article:
            self.render('404.html', message="无此文章！")
            return
        self.db.delete(article)
        self.db.commit()
        self.redirect('/')
