# Yelp Search
## Status
**Work in progress**

## Introduction
The purpose of this project is unclear at this point. Right now, it's just to use the API a bit and test out the GET functionality of Yelp's API.

Currently, a Python executable is able to make a call to Yelp's search or business API with a single term and location (note, while possible to use a business call, there is a high likelihood that a call with the `business` search term will return unexpected results. Optional arguments include the total number of results desired in return (making separate 20 record calls) and where in the search term string one wants to start. 

Resulting output is either created or appended -- depending on whether the output file exists -- in an `output` directory that is in the current working directory (if the `output` folder does not exist, the program will create it).

## Usage
```python
./run-yelp-search --search_type search --term Restaurants --location Philadelphia --nbr_results 200 --start 100
```