from bottle import (
    route, run, template, request, redirect
)

from scrapper import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    id = request.query.id
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.commit()
    if request.query.classify == 'True':
        redirect('/classify')
    else:
        redirect('/news')

@route("/update")
def update_news():
    update_news = get_news()
    authors = [news['author'] for news in update_news]
    titles = s.query(News.title).filter(News.author.in_(authors)).subquery()
    created_news = s.query(News).filter(News.title.in_(titles)).all()
    for news in update_news:
        if not created_news or news not in created_news:
            fill(news)
    redirect("/news")

@route("/classify")
def classify_news():
    marked_news = s.query(News).filter(News.title not in x_train and News.label != None).all()
    x_extra_train = [row.title for row in marked_news]
    y_extra_train = [row.label for row in marked_news]
    classifier.fit(x_extra_train, y_extra_train)

    blank_rows = s.query(News).filter(News.label == None).all()
    x = [row.title for row in blank_rows]
    labels = classifier.predict(x)
    classified_news = [blank_rows[i] for i in range(len(blank_rows)) if labels[i] == 'good']
    return template('recommendations', rows=classified_news)

    if __name__ == "__main__":
        s = session()
        classifier = NaiveBayesClassifier()
        marked_news = s.query(News).filter(News.label != None).all()
        x_train = [row.title for row in marked_news]
        y_train = [row.label for row in marked_news]
        classifier.fit(x_train, y_train)
        run(host="localhost", port=8080)
