from flask import Flask,render_template,request
import pandas as pd
# from pandas_profiling import ProfileReport

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])  # To render Homepage
def home_page():
    return render_template('index.html')

# @app.route('/Success', methods=['POST'])
def getting_file():
    # if request.method=='POST':
    file = request.files['file']
    file.save(file.filename)
    return file.filename

@app.route("/show", methods=["POST"])
def eda_analysis():
    if request.method=="POST":
        file_name = getting_file()
        df = pd.read_csv(file_name)
        return render_template('EDA.html', tables=[df.to_html()], titles=[' '], file=file_name)

if __name__ == '__main__':
    app.run(debug=True)
