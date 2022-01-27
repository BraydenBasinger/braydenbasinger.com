from website import create_app

app = create_app()

@app.route('/')
def main(): 
    return render_template("main.html")

@app.route('/about')
def about(): 
    return render_template("about.html")  

if __name__ == "__main__":
    app.run(debug=True, port=8000)