from flask import Flask, render_template, request, jsonify
import pickle
from build_model import * 

app = Flask(__name__)


with open('static/model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['GET'])
def index():
    """Render a simple splash page."""
    # return render_template('index.html')
    return render_template('submit.html')


@app.route('/submit', methods=['GET'])
def submit():
    """Render a page containing a textarea input where the user can paste an
    article to be classified.  """
    return render_template('submit.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Recieve the article to be classified from an input form and use the
    model to classify.
    """
    # breakpoint()
    data = str(request.form['article_body'])
    # print("User entered: ", data)
    # clean = str(model.clean_description([data])) #[0]) #passes description as a string array of words
    # tokenize = str(model.clean_description([clean])) #clean_description
    sentiment = str(model.sentiment([data])) #[0]) #passes description as a string array of words
    # print("sentiment:", sentiment)
    pred = str(model.predict([data])[0])
    return render_template('predict.html', article=data, predicted=pred)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
#
