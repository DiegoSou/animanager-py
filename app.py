from src.main import app, db
from src.infra.entities import Animals

app.app_context().push()
db.create_all()
