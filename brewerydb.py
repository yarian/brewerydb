import requests

DEFAULT_BASE_URI = "http://api.brewerydb.com/v2"
BASE_URI = ""
API_KEY = ""

simple_endpoints = ["beers", "breweries", "categories", "events", 
                    "featured", "features", "fluidsizes", "glassware",
                    "locations", "guilds", "heartbeat", "ingredients",
                    "search", "socialsites", "styles"]
    
single_param_endpoints = ["beer", "brewery", "category", "event",
                          "feature", "glass", "guild", "ingredient",
                          "location", "socialsite", "style", "menu"]

class BreweryDb:
    
    @staticmethod
    def __make_simple_endpoint_fun(name):
        @staticmethod
        def _function(options={}):
            return BreweryDb._get("/" + name, options)
        return _function

    @staticmethod
    def __make_singlearg_endpoint_fun(name):
        @staticmethod
        def _function(id, options={}):
            return BreweryDb._get("/" + name + "/" + id, options)
        return _function

    @staticmethod
    def _get(request, options):
        options.update({"key" : BreweryDb.API_KEY})
        return requests.get(BreweryDb.BASE_URI + request, params=options).json()
    
    @staticmethod
    def configure(apikey, baseuri=DEFAULT_BASE_URI):
        BreweryDb.API_KEY = apikey
        BreweryDb.BASE_URI = baseuri
        for endpoint in simple_endpoints:
            fun = BreweryDb.__make_simple_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint, fun)
        for endpoint in single_param_endpoints:
            fun = BreweryDb.__make_singlearg_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint, fun)
