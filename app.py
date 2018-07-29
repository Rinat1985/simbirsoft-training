import datetime

from flask import (Flask, request, render_template,
                   redirect, url_for, flash)


app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'
app.debug = True

posts = [
    {
        'created': datetime.datetime(2018, 6, 13, 13, 00, 00),
        'author': 'andrey',
        'title': 'Маргарита',
        'topic': 'Управление',
        'body': 'Тесто с томатной основой, покрытое сыром моцарелла.',
        'status': 'Неопределен'
    },
    {
        'created': datetime.datetime(2018, 6, 13, 19, 45, 43),
        'author': 'alexey',
        'title': 'Наполетана',
        'topic': 'Развитие',
        'body': 'Сочетание анчоусов с томатной пастой и сыром.',
        'status': 'Неопределен'
    },
    {
        'created': datetime.datetime(2018, 6, 14, 1, 48, 00),
        'author': 'aleks',
        'title': 'Веронез',
        'topic': 'Развитие',
        'body': 'Грибная лепёшка.',
        'status': 'Неопределен'
    },
    {
        'created': datetime.datetime(2018, 6, 18, 2, 10, 00),
        'author': 'mike',
        'title': 'По-апульски',
        'topic': 'Природа',
        'body': 'Луковая пицца с оливками, томатами и сыром.',
        'status': 'Неопределен'
    },
    {
        'created': datetime.datetime(2018, 6, 18, 2, 15, 00),
        'author': 'nike',
        'title': 'Четыре сыра',
        'topic': 'Спорт',
        'body': '«Очень сырное» блюдо, в состав которого входит пармезан, рикотта, горгонзола и моцарелла. ',
        'status': 'Неопределен'
    },
]


@app.route('/')
def index():
    print(posts[4]['status'])
    return render_template('posts.html', posts=reversed(posts))


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        post = {
            'created': datetime.datetime.now(),
            'author': request.form['author'],
            'title': request.form['optionsRadios'],
            'body': "12344", #request.form['body'],
            'topic': "123",#request.form['topic']
            'status': "Неопределен"
        }
        posts.append(post)

        flash('Новый пост добавлен')

        return redirect(url_for('index'))
    else:
        return render_template('add_post.html')


@app.route('/author/<string:author>')
def author(author):
    author_posts = [post for post in posts if post['author'] == author]

    return render_template('author.html',
                           author=author,
                           posts=author_posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/status/<string:author>', methods=['POST', 'GET'])
def status(author):
    if request.method == 'POST':
        current = 0
        for post in posts:
            if post['author'] == author:
                print(current)
                break
            current = current + 1
        posts[current] = {
            'created': datetime.datetime.now(),
            'author':  posts[current]['author'],
            'title':   posts[current]['title'],
            'body':    posts[current]['body'],
            'topic':   posts[current]['topic'],
            'status':  request.form['optionsRadios']
        }
        flash('Статус изменен')
        flash(posts[current]['status'])

        return redirect(url_for('index'))
    else:
       return render_template('status.html', author=author)