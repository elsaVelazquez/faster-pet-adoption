
from flask import Flask, render_template, request, jsonify
# from flask_bootstrap import Bootstrap
import pickle
from predict_one import TextClassifier

#instantiate the class
clf = TextClassifier()

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    """Render a simple splash page."""
    # return render_template('index.html')
    return render_template('submit.html')


@app.route('/submit', methods=['GET'])
def submit():
    """Render a page containing a textarea input where the user can paste an
    description to be classified.  """
    return render_template('submit.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Recieve the description to be classified from an input form and use the
    model to classify.
    """
    
    # breakpoint()
    data = str(request.form['article_body'])

    pred = str(clf.predict_one([data])) #[0])
    # twit = str(clf.predict_one_twitter([data]))#[0])
    tf = (clf.tfidf_([data]))#[0] #.any()
    return render_template('predict.html', description=data, predicted=pred, cosim=tf) #, twitter=twit)


@app.route('/about', methods=['GET'])
def about():
    """More about this project """
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    """contact Elsa"""
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
    

