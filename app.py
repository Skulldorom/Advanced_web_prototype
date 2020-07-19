from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():    
    from hobby_tracker import test_data, load_ints
    test_data()
    return render_template("index.html",data = load_ints())

@app.route('/reset')
def reset():
    from hobby_tracker import create_empty
    create_empty()
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()