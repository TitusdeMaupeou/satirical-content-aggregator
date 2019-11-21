from flask import Flask, render_template
from aggregation import soup, article_list

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', article_list=article_list)

if __name__ == '__main__':
    app.run(debug=True)