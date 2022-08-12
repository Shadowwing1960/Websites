from Website import create_app


# starting website 
def website():
    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)


# Running website
website()
