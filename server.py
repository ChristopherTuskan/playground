from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html',color = 'blue', num = 3)

@app.route('/play/<int:x>')
def playNum(x):
    return render_template('index.html',color = 'blue', num = x)

@app.route('/play/<int:x>/<boxColor>')
def playColor(x,boxColor):
    return render_template('index.html',color = boxColor, num = x)




if __name__ == '__main__':
    app.run(debug=True)