from app import create_app


app = create_app()

    # No need for app.run() in production
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))