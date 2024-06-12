from config import create_app


app = create_app()
app.config['LOGIN_DISABLED'] = True

if __name__ == '__main__':
    app.run(port=5000,debug=True)