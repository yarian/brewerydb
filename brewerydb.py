import requests

DEFAULT_BASE_URI = "http://api.brewerydb.com/v2"
BASE_URI = ""
API_KEY = ""

class BreweryDb:

    @staticmethod
    def _apply_apikey(options):
        options.update({"key" : BreweryDb.API_KEY})
        return options

    @staticmethod
    def _get(request, options):
        return requests.get(BreweryDb.BASE_URI + request, params=options).text

    @staticmethod
    def beers(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/beers", options)

    @staticmethod
    def beer(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/beer/" + id, options)

    @staticmethod
    def breweries(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/breweries", options)

    @staticmethod
    def brewery(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/brewery/" + id, options)
    
    @staticmethod
    def categories(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/categories", options)

    @staticmethod
    def category(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/category/" + id, options)

    @staticmethod
    def events(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/events", options)

    @staticmethod
    def event(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/event/" + id, options)

    @staticmethod
    def featured(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/featured", options)

    @staticmethod
    def features(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/features", options)

    @staticmethod
    def feature(yearweek, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/feature/" + yearweek, options)

    @staticmethod
    def fluidsizes(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/fluidsizes", options)

    @staticmethod
    def fluidsize(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/fluidsize/" + id, options)

    @staticmethod
    def glassware(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/glassware", options)
    
    @staticmethod
    def glass(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/glass/" + id, options)

    @staticmethod
    def guilds(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/guilds", options)
    
    @staticmethod
    def guild(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/guild/" + id, options)

    @staticmethod
    def heartbeat(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/heartbeat", options)

    @staticmethod
    def ingredients(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/ingredients", options)
    
    @staticmethod
    def ingredient(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/ingredient/" + id, options)

    @staticmethod
    def locations(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/locations", options)
    
    @staticmethod
    def location(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/location/" + id, options)

    @staticmethod
    def menu(menu_type, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/menu" + menu_type, options)

    @staticmethod
    def search(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/search", options)

    @staticmethod
    def socialsites(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/socialsites", options)

    @staticmethod
    def socialsite(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/socialsite/" + id, options)

    @staticmethod
    def styles(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/styles", options)

    @staticmethod
    def style(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/brewery/" + style, options)
    
    @staticmethod
    def set_apikey(apikey):
        BreweryDb.API_KEY = apikey

    @staticmethod
    def configure(apikey, baseuri=DEFAULT_BASE_URI):
        BreweryDb.API_KEY = apikey
        BreweryDb.BASE_URI = baseuri
