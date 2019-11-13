from flask import Flask
import sample

app = Flask(__name__)

@app.route('/')
def index():
    '''This function calls the histogram function on a sample text. This will then pick a 
    random word and return it'''
    text = sample.get_text()
    histo = sample.histogram(text)
    random_words = sample.sample_frequency(histo)
    
    return random_words


if __name__ == "__main__":
    app.run(debug=False)