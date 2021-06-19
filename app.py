#app.py the ORFLASK version of a microblog
''' A Flask app which showcases a microblog'''

from flask import Flask, url_for, render_template
app = Flask(__name__)



posts = [
    { 
     'post_number' : 1,
     'post_title' : 'Post1',
     'post_date' : 'dtg1',
     'post_content': 'This is content 1',
     'post_tag' : 'python'
        
    },
    
    {
          'post_number' : 2,
     'post_title' : 'Post2',
     'post_date' : 'dtg2',
     'post_content': 'This is content 2',
     'post_tag' : 'python'   
    },
    
    {
    'post_number' : 3,
    'post_title' : 'Post3',
    'post_date' : 'dtg3',
    'post_content': 'This is content 3',
    'post_tag' : 'python'
    },
]






@app.route('/')
def index():
    title = 'Oz Rhodes'
    
    return render_template('index.html')

@app.route('/blog')
def blog():
    title = 'OR - Blog'
    return render_template('blog.html',title = title, posts = posts)

@app.route('/about')
def about():
    title = 'OR - About'
    return render_template('about.html' ,title = title)

@app.route('/contact')
def contact():
    title = 'OR - Contact'
    return render_template('contact.html' ,title = title)

@app.route('/category')
def category():
    title = 'OR - Category'
    return render_template('category.html',title = title)
