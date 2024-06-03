

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/yourdatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from models import DataModel  # Import models after initializing the app

    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.before_first_request
    def create_tables():
        db.create_all()
        with open('data/jsondata.json') as f:
            data = json.load(f)
            for item in data:
                data_entry = DataModel(
                    intensity=item.get('intensity'),
                    likelihood=item.get('likelihood'),
                    relevance=item.get('relevance'),
                    year=item.get('year'),
                    country=item.get('country'),
                    topic=item.get('topic'),
                    region=item.get('region'),
                    city=item.get('city'),
                    sector=item.get('sector'),
                    pestle=item.get('pestle'),
                    source=item.get('source'),
                    swot=item.get('swot')
                )
                db.session.add(data_entry)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)





# # backend/app.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/yourdatabase'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from models import DataModel  # Import the DataModel
# from routes import main as main_blueprint
# app.register_blueprint(main_blueprint)

# @app.before_first_request
# def create_tables():
#     db.create_all()
#     with open('data/jsondata.json') as f:
#         data = json.load(f)
#         for item in data:
#             data_entry = DataModel(
#                 intensity=item.get('intensity'),
#                 likelihood=item.get('likelihood'),
#                 relevance=item.get('relevance'),
#                 year=item.get('year'),
#                 country=item.get('country'),
#                 topic=item.get('topic'),
#                 region=item.get('region'),
#                 city=item.get('city'),
#                 sector=item.get('sector'),
#                 pestle=item.get('pestle'),
#                 source=item.get('source'),
#                 swot=item.get('swot')
#             )
#             db.session.add(data_entry)
#         db.session.commit()

# if __name__ == '__main__':
#     app.run(debug=True)
