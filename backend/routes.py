from flask import Blueprint, jsonify
from models import DataModel

main = Blueprint('main', __name__)

@main.route('/api/data', methods=['GET'])
def get_data():
    data = DataModel.query.all()
    data_list = [
        {
            'intensity': item.intensity,
            'likelihood': item.likelihood,
            'relevance': item.relevance,
            'year': item.year,
            'country': item.country,
            'topic': item.topic,
            'region': item.region,
            'city': item.city,
            'sector': item.sector,
            'pestle': item.pestle,
            'source': item.source,
            'swot': item.swot
        }
        for item in data
    ]
    return jsonify(data_list)






# # backend/routes.py
# from flask import Blueprint, jsonify
# from models import DataModel

# main = Blueprint('main', __name__)

# @main.route('/api/data', methods=['GET'])
# def get_data():
#     data = DataModel.query.all()
#     data_list = [
#         {
#             'intensity': item.intensity,
#             'likelihood': item.likelihood,
#             'relevance': item.relevance,
#             'year': item.year,
#             'country': item.country,
#             'topic': item.topic,
#             'region': item.region,
#             'city': item.city,
#             'sector': item.sector,
#             'pestle': item.pestle,
#             'source': item.source,
#             'swot': item.swot
#         }
#         for item in data
#     ]
#     return jsonify(data_list)





# # # backend/routes.py
# # from flask import Blueprint, jsonify
# # from app import db, DataModel

# # main = Blueprint('main', __name__)

# # @main.route('/data', methods=['GET'])
# # def get_data():
# #     data = DataModel.query.all()
# #     results = [
# #         {
# #             "intensity": entry.intensity,
# #             "likelihood": entry.likelihood,
# #             "relevance": entry.relevance,
# #             "year": entry.year,
# #             "country": entry.country,
# #             "topic": entry.topic,
# #             "region": entry.region,
# #             "city": entry.city,
# #             "sector": entry.sector,
# #             "pestle": entry.pestle,
# #             "source": entry.source,
# #             "swot": entry.swot
# #         } for entry in data]

# #     return jsonify(results)
