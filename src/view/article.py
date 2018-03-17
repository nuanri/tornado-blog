from sqlalchemy import desc

from handler import BaseHandler
from model.article import Article
from form.article import ArticleForm


class IndexHandler(BaseHandler):

    def get(self):
        articles = self.db.query(Article).order_by(desc(Article.id)).all()
        self.render('index.html', articles=articles)


class CreateHandler(BaseHandler):

    def get(self):
        self.render('article/create.html')

    def post(self):
        form = ArticleForm(self)
        if form.validate():
            article = Article(title=form.title.data, content=form.content.data)
            self.db.add(article)
            self.db.commit()
            self.redirect('/')
            # self.render("article/detail.html", article=article)


class DetailHandler(BaseHandler):

    def get(self, ID):

        article = self.db.query(Article).filter_by(id=ID).one()

        self.render("article/detail.html", article=article)

    def post(self, ID):
        form = ArticleForm(self)

        article = self.db.query(Article).filter_by(id=ID).one()
        form.title.data = article.title
        form.content.data = article.content


class EditHandler(BaseHandler):
    def get(self):
        pass


class DeleteHandler(BaseHandler):
    def get(self):
        pass
