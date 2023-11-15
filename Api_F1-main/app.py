from flask import Flask, render_template 

app = Flask(__name__) 

from f1 import response_constructor, response_drivers, response_races 

@app.route('/') 
def home(): 
    return render_template('index.html', data=response_drivers.json(), constructor=response_constructor.json(), races=response_races.json()) 

if __name__ == '__main__':
    app.run(debug=True)

