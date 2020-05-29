# Pangeo STAC Catalog
This repository contains a copy of Pangeo's [cloud data catalog](https://github.com/pangeo-data/pangeo-datastore), formatted to follow the [SpatioTemporal Asset Catalog (STAC) specification](https://github.com/radiantearth/stac-spec).
The root STAC catalog can be found at:
```
https://raw.githubusercontent.com/charlesbluca/pangeo-datastore-stac/master/master/catalog.json
```
Though the catalogs do not yet contain any accessible data, in time they will be able to hold:
- Zarr groups/arrays (through a [pending Zarr extension for STAC](https://github.com/radiantearth/stac-spec/issues/781))
- Earth System Model (ESM) collections (through a [pending ESM extension for STAC](https://github.com/ncar/esm-collection-spec/issues/21))
- CSV-based dataframes

## Motivations
The motivation behind this project is to have a version of the current cloud data catalog which can be searched and browsed regardless of language.
At the moment, the current YAML-based catalogs are only accessible through Python using [intake](https://github.com/intake/intake).
This means that any server-side code accessing these catalogs must be written in Python, which has historically played a big role in how we have generated the website containing previews of all catalogged data:
- Originally, the website was created using a [static site generator](https://github.com/pangeo-data/pangeo-datastore/blob/master/build_catalog_rst.py); however, this approach ran into issues once we began catalogging data which authentication to be accessed, which could not be done through GitHub.
- We later moved to a [dynamic Flask-based website](https://github.com/pangeo-data/pangeo-datastore-flask/), powered by [Google App Engine](https://cloud.google.com/appengine); this allowed us to get the proper authentication to load dataset previews on-demand, but frequently ran into memory issues which made many datasets impossible to view.

With the introduction of [intake-stac](https://github.com/pangeo-data/intake-stac), an intake extension which allows Python users to browse STAC catalogs, there is no longer a need to for the catalogs themselves to be tied to intake.
Thus, a move to JSON-based STAC catalogs allows a variety of new languages (in particular JavaScript, Ruby, and PHP) access to the catalogs, without leaving behind initial Python users.

## Guidelines (subject to change)
**All of the Pangeo STAC catalogs are working with version 0.9.0 of the STAC specification.**

Currently, the Pangeo STAC catalog follows STAC specifications for an [absolute published catalog](https://github.com/radiantearth/stac-spec/blob/master/best-practices.md#published-catalogs).
All preexisting intake catalogs correspond to [STAC catalogs](https://github.com/radiantearth/stac-spec/tree/master/catalog-spec), while datasets and data collections correspond to [STAC collections](https://github.com/radiantearth/stac-spec/tree/master/collection-spec) with extensions required to access the data being listed under the `stac_extensions` field.

## Progress
There is still a lot of work to be done before this catalog can be considered equivalent to the current cloud data catalog.
In particular:

- [ ] Finishing the specifications for the Zarr/ESM extensions to allow these data to be represented in collections.
- [ ] Filling in missing/empty fields in the catalog/collections (such as `description`, `extent`, `providers`, and licensing links)
- [ ] Making sure the catalogs validate using [stac-validator](https://github.com/sparkgeo/stac-validator) in conjunction with continuous integration
- [ ] Making sure that validated catalogs can be accessed using intake-stac
