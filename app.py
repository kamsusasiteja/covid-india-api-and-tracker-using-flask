from flask import Flask,render_template
from covid_india import states
app = Flask(__name__)

@app.route('/')
def hello_world():
    state=input('enter state')
    data=states.getdata(state)
    return render_template('index.html',data=data)
    
if __name__=="__main__":
    app.run(debug=True)