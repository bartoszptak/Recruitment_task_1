from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
   return render_template('index.html')

@app.route('/check', methods=['POST', 'GET'])
def check():
    if request.method == 'POST': 
        data = request.json
        controller = Controller()


        error = controller.check_data(data)
        
        if error:
           report_template = render_template('reports.html', decision=error)
           return report_template 

        
        decision = controller.get_decision(data)

        report_template = render_template('reports.html', decision=decision)

    return report_template  

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')   
