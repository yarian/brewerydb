# BreweryDB API Python Wrapper

This is a simple wrapper around the BreweryDB API packaged as a Python module.

* Wraps all GET requests found in the [API documentation](http://developer.pintlabs.com/brewerydb/api-documentation) as of 10/25/2012.
* You will need to [register for an API key](http://www.brewerydb.com/api/register).

Remember: Good People Drink Good Beer!

# Version

* 1.1 Reimplemented wrapper using reflection and updated README.
* 1.0 Initial release

# Todo

#### By Priority

* Find elegant way to support post requests

# Dependencies

* [Requests](http://docs.python-requests.org/en/latest/)

# Notes

This wrapper uses reflection to instantiate its methods at runtime.
This was done to avoid huge amounts of code duplication. However, it
also has the added benefit of allowing you to extend it without
modifying it. Simply call one of:

    __make_simple_endpoint_fun(name)
    __make_singlearg_endpoint_fun(name)

This will generate a new function called name that creates a new request
to: BreweryDb base url `+ "/" + name`. 

If your name has slashes in it, it will turn those into underscores for the method name.
So for example, the method for the `search/upc` endpoint would be `search_upc`.

# Usage

    from brewerydb import *
    BreweryDb.configure(apikey[, baseuri])

It is important that configure is called before calling any of the
other methods. Methods are created at runtime during configure.

If you see an error:
    AttributeError: class BreweryDb has no attribute X

You most likely did not call BreweryDb.configure.

# Code Examples

### Fetching all beers:

    BreweryDb.beers()

### Getting a list of beers on a specific page:

    BreweryDb.beers({'page':10})

### Searching for beers with a specific query:

    BreweryDb.search({'type':'beer','q':'unibroue'})

### Getting a specific beer or brewery by ID:

    BreweryDb.beer(O3tmVI)

### Getting all the breweries around Seattle, WA:

    BreweryDb.breweries({'geo':1,
                         'lat':47.6097,
                         'lng':-122.3331,
                         'radius':30,
                         'units':'m'})
