from src.main import app, db, animals_routes

# Rotas Blueprints
app.register_blueprint(animals_routes)

# Hello world
@app.route("/", methods=["GET"])
def hello_world():
    """hello"""
    return 'Hello World'

app.app_context().push()
db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
