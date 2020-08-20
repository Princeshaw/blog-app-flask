from  flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/post')
def post():
    return render_template('post.html')
@app.route('/contact')
def contact():
   return render_template('contact.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)