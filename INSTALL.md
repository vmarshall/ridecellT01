**Docker Command For Test Database**

docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5433:5432 kartoza/postgis:9.6-2.4


**quick-test.sh has basic external rest commands for testing**

***Check Against Known SF locations***

curl "http://127.0.0.1:8000/api/v1/parking/?point=-122.4862,37.7694&dist=500000"
curl "http://127.0.0.1:8000/api/v1/parking/?point=-122.4862,37.7694&dist=10000"
curl "http://127.0.0.1:8000/api/v1/parking/?point=-122.4862,37.7694&dist=9000"
curl "http://127.0.0.1:8000/api/v1/parking/?point=-122.4862,37.7694&dist=8000"

***API Entry Point***

http://127.0.0.1:8000/api/v1/parking/

***API Documetation URL (CRUD operations for ParkingSpot Objects)***
http://127.0.0.1:8000/api/v1/docs/#parking-list

***Swagger View of API***

http://127.0.0.1:8000/schema/

***Fixture Data***
data.json has some well-know SF locations for spot checking