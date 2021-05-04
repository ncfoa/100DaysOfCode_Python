import requests
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import datetime

CONFIG = dotenv_values(".env")

# UNCOMMENT THE BELOW TO CREATE A NEW USER #

# BEGIN USER CREATION #

# pixela_endpoint = f'https://pixe.la/v1/users' # USER CREATION Endpoint
#
#
# user_params = {
#     "token": CONFIG["PIXELA_TOKEN"],  # Change this to be your choice of token.
#     "username": CONFIG["PIXELA_USER"],  # Change this to be your choice of username
#     "agreeTermsOfService": "yes",  # If you don't agree with their TOS, might as well stop now.
#     "notMinor": "yes"  # If you are considered a minor in your country then change to "no"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)  # Make the request to create user.
# print(response.text)  # Print out the response in the console to see if your name was allowed.

# END USER CREATION #

# UNCOMMENT BELOW LINES TO CREATE A NEW GRAPH #
# BEGIN GRAPH CREATION #

# pixela_endpoint = f'https://pixe.la/v1/users/{CONFIG["PIXELA_USER"]}/graphs'  # Create New Graph Endpoint
#
# header = {
#     "X-USER-TOKEN": CONFIG["PIXELA_TOKEN"],  # For Login Purposes
# }
#
# graph_config = {
#     "id": "goofingoff1",  # REQUIRED
#     "name": "Goofing Off",  # REQUIRED
#     "unit": "hour",  # REQUIRED
#     "type": "float",  # REQUIRED
#     "color": "ajisai",  # REQUIRED
#     "timezone": "US/Central"  # OPTIONAL defaults to UTC
# }
#
# response = requests.post(url=pixela_endpoint, json=graph_config, headers=header)  # Create graph
# print(response.text)  # Check if Successful

# END GRAPH CREATION #

# UNCOMMENT THE BELOW TO UPDATE A GRAPH #
# BEGIN PIXEL CREATION #

pixela_endpoint = f'https://pixe.la/v1/users/{CONFIG["PIXELA_USER"]}/graphs/goofingoff1'

header = {
    "X-USER-TOKEN": CONFIG["PIXELA_TOKEN"],  # For login purposes
}
minutes = str(input("How many minutes did you goof off today? "))
date = str(datetime.date.today()).replace("-", "")
# date = datetime.datetime(year=2021, month=4, day=26).strftime("%Y%m%d")
# print(date)
pixel_config = {
    "date": date,
    "quantity": minutes
}

response = requests.post(url=pixela_endpoint, json=pixel_config, headers=header)
print(response.text)

# UPDATE GRAPH DATAPOINTS

# pixela_endpoint = f'https://pixe.la/v1/users/{CONFIG["PIXELA_USER"]}/graphs/goofingoff1'
#
# header = {
#     "X-USER-TOKEN": CONFIG["PIXELA_TOKEN"],  # For login purposes
# }
#
# data = {
#     "unit": "Minutes"
# }
#
# response = requests.put(url=pixela_endpoint, headers=header, json=data)
# print(response.text)
