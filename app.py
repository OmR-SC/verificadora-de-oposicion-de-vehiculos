from flask import Flask
from src.routes.ValidatorRoutes import validator_page

app = Flask(__name__)

#Routes
app.register_blueprint(validator_page)

if __name__ == '__main__':
    app.run(debug=True)
