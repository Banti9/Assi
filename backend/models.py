from app import db

class DataModel(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Integer)
    likelihood = db.Column(db.Integer)
    relevance = db.Column(db.Integer)
    year = db.Column(db.Integer)
    country = db.Column(db.String(64))
    topic = db.Column(db.String(64))
    region = db.Column(db.String(64))
    city = db.Column(db.String(64))
    sector = db.Column(db.String(64))
    pestle = db.Column(db.String(64))
    source = db.Column(db.String(64))
    swot = db.Column(db.String(64))

    def __init__(self, intensity, likelihood, relevance, year, country, topic, region, city, sector, pestle, source, swot):
        self.intensity = intensity
        self.likelihood = likelihood
        self.relevance = relevance
        self.year = year
        self.country = country
        self.topic = topic
        self.region = region
        self.city = city
        self.sector = sector
        self.pestle = pestle
        self.source = source
        self.swot = swot










# # backend/models.py
# from app import db

# class DataModel(db.Model):
#     __tablename__ = 'data'

#     id = db.Column(db.Integer, primary_key=True)
#     intensity = db.Column(db.Integer)
#     likelihood = db.Column(db.Integer)
#     relevance = db.Column(db.Integer)
#     year = db.Column(db.Integer)
#     country = db.Column(db.String(64))
#     topic = db.Column(db.String(64))
#     region = db.Column(db.String(64))
#     city = db.Column(db.String(64))
#     sector = db.Column(db.String(64))
#     pestle = db.Column(db.String(64))
#     source = db.Column(db.String(64))
#     swot = db.Column(db.String(64))

#     def __init__(self, intensity, likelihood, relevance, year, country, topic, region, city, sector, pestle, source, swot):
#         self.intensity = intensity
#         self.likelihood = likelihood
#         self.relevance = relevance
#         self.year = year
#         self.country = country
#         self.topic = topic
#         self.region = region
#         self.city = city
#         self.sector = sector
#         self.pestle = pestle
#         self.source = source
#         self.swot = swot
