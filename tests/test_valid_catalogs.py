import pytest
from requests import get
from json import load
from glob import glob
from jsonschema import validate

# fetch relevant STAC schemas
catalog_schema = get('https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/json-schema/catalog.json').json()
collection_schema = get('https://raw.githubusercontent.com/radiantearth/stac-spec/master/collection-spec/json-schema/collection.json').json()

# replace relative link in collection schema
collection_schema['allOf'][0]['$ref'] = 'https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/json-schema/catalog.json'

# validate catalogs
catalogs = glob('../**/catalog.json', recursive=True)
collections = glob('../**/collection.json', recursive=True)

@pytest.mark.parametrize('path', catalogs)
def test_catalogs(path):
    
    with open(path, 'r') as f:
        catalog = load(f)
        
    validate(catalog, catalog_schema)
    
@pytest.mark.parametrize('path', collections)
def test_collections(path):
    
    with open(path, 'r') as f:
        collection = load(f)
        
    validate(collection, collection_schema)
