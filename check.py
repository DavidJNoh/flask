from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    user= (
        {'first_name':'Michael','last_name':'Choi'},
        {'first_name':'John','last_name':'Supsupsin'},
        {'first_name':'Mark','last_name':'Guillen'},
        {'first_name':'KB','last_name':'Tonel'},
    )
    return render_template('checkindex.html')

if __name__=="__main__":
    app.run(debug=True)