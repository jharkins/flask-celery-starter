from project import create_app, ext_celery, socketio

app = create_app()
celery = ext_celery.celery


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    socketio.run(
        app,
        debug=True,
        use_reloader=True,
        host='0.0.0.0',
        allow_unsafe_werkzeug=True,
    )
