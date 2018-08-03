# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    },
    {
        "lat": 42,
        "lon": -333,
        "name": "a new world"
    }
]

# Write a loop that prints out all the field values for all the waypoints
# print([key for key in waypoints])
for i in waypoints: 
    print(i["lat"])
    print(i["lon"])
    print(i["name"])
# Add a new waypoint to the list
