import influxdb_client, os, sys, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import urllib.request


# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# import count_person function
from yolo import count_person
from line import send_line



def main():
    # .env path
    path = os.path.join(os.path.dirname(__file__), '..')
    sys.path.append(path)

    # load .env file
    load_dotenv()

    

    # get env variables
    influx_token = os.getenv('INFLUX_TOKEN')
    org = os.getenv('INFLUX_ORG')

    # get URL form .env
    influx_url = os.getenv('INFLUX_URL')
    camera_url = os.getenv('CAMERA_URL')

    # image name
    save_as = 'image.jpg'



    # `line notify` token
    line_token = os.getenv('LINE_TOKEN')
 
 

    client = influxdb_client.InfluxDBClient(url=influx_url, token=influx_token, org=org)
    
    bucket="WATCHING_YOU"
    
    write_api = client.write_api(write_options=SYNCHRONOUS)
       
    while True:
        urllib.request.urlretrieve(camera_url, save_as)
        num_of_person = count_person(save_as)

        # create message
        msg = 'Number of Persons: ' + str(num_of_person)


        # send notification
        send_line(line_token, msg)


        point = (
            Point("Persons")
            .tag("tagname1", "tagvalue1")
            .field("field1", num_of_person)
        )
        write_api.write(bucket=bucket, org=org, record=point)
        time.sleep(15) # separate points by 1 second
    



if __name__ == '__main__':
    main()
