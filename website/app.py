from flask import Flask, request, render_template, flash
from tags_generator import TagsGenerator
import os
app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

openai_api_key = os.environ.get('API_URL')
tg = TagsGenerator(openai_api_key)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        if(len(body)<100):
            flash('not enough input')
            return render_template('index.html', tags=[], title = title, body = body)
        text = title + body
        print(text)
        tags = tg.generate_tags(text)
        #tags = ['test1', 'test2', 'test3', 'test4', 'test5']
        return render_template('index.html', tags=tags,  body=body, title=title)
    else: 
        return render_template('index.html', tags=[], title = '', body = '')
        


if __name__ == "__main__":
    app.run(debug=True)
