This is incomplete.

== BreweryDB API

This is a simple wrapper around the BreweryDB API packaged as a Python class.

* Wraps all the API documented here: http://www.brewerydb.com/api/documentation
* You will need to register for an API key: http://www.brewerydb.com/api/register
* You can pass any of the options specified in the BreweryDB API

Remember: Good People Drink Good Beer!

== Releases

0.0.0
* TODO

== Examples

You can fetch beers:

  response = BreweryDb.beers

Get a list of beers on a specific page:

  response = BreweryDb.beers({'page':10,'metadata':true) 

Searching for Beers:

  results = BreweryDb.search({'q':'stone'})

Get a specific beer or brewery by id:

  response = BreweryDb.beer(1196)
  response = BreweryDb.brewery(1000)

Get all the breweries around Washington DC:

  response = BreweryDb.breweries({'geo':1,
                                 'lat':38.875532,
                                 'lng':-77.007294,
                                 'radius':30,
                                 'units':'m'})

Categories, Styles and Glassware work as well.

