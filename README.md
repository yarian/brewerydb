# BreweryDB API Python Wrapper

This is a simple wrapper around the BreweryDB API packaged as a Python module.

* Wraps all GET requests found in the [API documentation](http://developer.pintlabs.com/brewerydb/api-documentation) as of 10/25/2012.
* You will need to [register for an API key](http://www.brewerydb.com/api/register).

Remember: Good People Drink Good Beer!

# Version

* 0.1 Initial commit

# Todo

#### By Priority

* Add automated testing
* Constrain requests like menu to one of the valid endpoints

##### Other

* Find elegant way to support post requests
* Look into making a pip package(?)

# Dependencies

* [Requests](http://docs.python-requests.org/en/latest/)

# Usage

    from brewerydb import *
    BreweryDb.configure(apikey[, baseuri])

# Examples

### Fetching all beers:

    response = BreweryDb.beers()

### Getting a list of beers on a specific page:

    response = BreweryDb.beers({'page':10})

### Searching for beers:

    results = BreweryDb.search({'type':'beer','q':'stone'})

### Getting a specific beer or brewery by ID:

    response = BreweryDb.beer(1196)
    response = BreweryDb.brewery(1000)

### Getting all the breweries around Washington, DC:

    response = BreweryDb.breweries({'geo':1,
                                    'lat':38.875532,
                                    'lng':-77.007294,
                                    'radius':30,
                                    'units':'m'})
