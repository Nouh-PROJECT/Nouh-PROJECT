from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/write_action')
def index():
    return render_template('index.html') 

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        writer = request.form['writer']
        content = request.form['content']
        
        return redirect(url_for('index')) 
    
    return render_template('write.html') 

if __name__ == '__main__':
    app.run(debug=True)
