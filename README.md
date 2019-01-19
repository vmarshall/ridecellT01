Project Description



Assume that we are building a street parking spot reservation service. Each parking spot is identified by its location (lat, lng). Users should be able to view street parking spots, reserve and pay for the parking spots or cancel their reservations. Build REST API's for the following and share the github repository with us.  You can populate your database with any dummy data you want. You can write the code in Python/Django, Ruby/Rails, JS/Express or in any other web framework you prefer, but Python/Django is preferred.



Requirements

Search for an address and find nearby parking spot. (input: lat, lng, radius in meters. Output - list of parking spots within the radius).
Reserve a parking spot
Bonus

Automated tests

Sample API requests/responses:
GET /api/v1/parking/available?lat=37.xxx&lng=-122.adsf&radius=2.0 

Response



{



	{

		id: 1,

		lat: <lat of the parking spot>

		lng: <lng of the parking spot>

                is_available: True

	},

	{

		id: 2,

		lat: <lat of the parking spot>

		lng: <lng of the parking spot>

                is_available: True

	},

}


POST /api/v1/parking/reserve?parking_id=1



Once you reserve parking spot 1, if you call the available api (first example endpoint), it should not return parking spot 1 as it is reserved.


