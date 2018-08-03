from flask import Flask, render_template  
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                           
def hello_world():
    return render_template('index.html') 

@app.route('/play')
def threebox():
    return render_template('play.html',times=3)

@app.route('/play/<times>')
def manybox(times):
    times=int(times)
    return render_template('play.html',times=times)

@app.route('/play/<times>/<color>')
def colorbox(times,color):
    times=int(times)
    return render_template('play.html',times=times,color=color)


if __name__=="__main__":
    app.run(debug=True)      