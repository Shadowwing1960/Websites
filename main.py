from Website import create_app


def website_start_up():
    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)


website_start_up()
