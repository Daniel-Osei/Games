from flask import Flask, render_template

app = Flask(__name__)
#------------------------------------------>

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bounce.html')
def bounce():
    return render_template('bounce.html')

@app.route('/lost.html')
def lost():
        return render_template('lost.html')

@app.route('/street.html')
def about():
        return render_template('street.html')


#-------------->
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


