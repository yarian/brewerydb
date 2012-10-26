import requests, json

DEFAULT_BASE_URI = 'http://api.brewerydb.com/v2'
BASE_URI = ''
API_KEY = ''

# API Default format is JSON at time of this writing

class BreweryDb:

    @staticmethod
    def _apply_apikey(options):
        options.update({"key" : API_KEY})
        return options

    @staticmethod
    def _get(request, options):
        return requests.get(BASE_URI + request, params=options).text

    @staticmethod
    def search(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/search", options)

    @staticmethod
    def breweries(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/breweries", options)

    @staticmethod
    def brewery(id, options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/brewery/" + id, options)
  
    @staticmethod
    def beers(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/beers", options)

    @staticmethod
    def beer(ids, options={}):
        BreweryDb._apply_apikey(options)
        options.update({"ids":",".join(ids)})
        return BreweryDb._get("/beer", options)
    
    @staticmethod
    def styles(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/styles", options)

    @staticmethod
    def style(id, options={}):
        BreweryDb._apply_apikey(options)
        options.update({"id":id})
        return BreweryDb._get("/brewery", options)
    
    @staticmethod
    def categories(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/categories", options)

    @staticmethod
    def category(id, options={}):
        BreweryDb._apply_apikey(options)
        options.update({"id":id})
        return BreweryDb._get("/category", options)

    @staticmethod
    def glassware(options={}):
        BreweryDb._apply_apikey(options)
        return BreweryDb._get("/glassware", options)
    
    @staticmethod
    def glass(id, options={}):
        BreweryDb._apply_apikey(options)
        options.update({"id":id})
        return BreweryDb._get("/glass", options)
    
    @staticmethod
    def set_apikey(apikey):
        API_KEY = apikey

    @staticmethod
    def configure(apikey, baseuri=DEFAULT_BASE_URI):
        API_KEY = apikey
        BASE_URI = baseuri
