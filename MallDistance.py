# SpencerP7.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/16/2024
# Purpose: This program calculates the distance between a user's location and two malls in Albuquerque.
# Python Version: 3.12.5


# Imports
import time
from Assignments.Reusable import Goodbye as gb
import math

# Create a class to manage geographic points and calculate distances
class GeoPoint:
    def __init__(self):
        self.lat = 0
        self.lon = 0
        self.description = ''

    # Set the latitude and longitude of the GeoPoint
    def SetPoint(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude

    # Return the latitude and longitude of the GeoPoint
    def GetPoint(self):
        return self.lat, self.lon

    # Calculate and return the distance between the GeoPoint and given coordinates
    def Distance(self, lat, lon):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1 = math.radians(self.lat), math.radians(self.lon)
        lat2, lon2 = math.radians(lat), math.radians(lon)

        # Spherical law of cosines formula
        dist = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
        return dist

    # Set the description of the GeoPoint
    def SetDescription(self, description):
        self.description = description

    # Return the description of the GeoPoint
    def GetDescription(self):
        return self.description

# Function Definitions
def display_header():
    print('Welcome to the Which Mall is Closer Calculator.')
    print('This program will calculate the distance between your location and one of ABQ\'s malls.')
    print('To start, enter your location in coordinates below.\n')


def cardinal_direction(lat, lon):
    # Determine the cardinal direction of the latitude
    lat_dir = 'N' if lat > 0 else 'S'
    # Determine the cardinal direction of the longitude
    lon_dir = 'E' if lon > 0 else 'W'
    return lat_dir, lon_dir


def display_results(description, point):
    lat, lon = point
    lat_dir, lon_dir = cardinal_direction(lat, lon)
    address = mall_addresses.get(description)
    print(f'The closest mall to you is: {description}\nLocated at: {address}\nWhich has coordinates of {abs(lat)}° {lat_dir}, {abs(lon)}° {lon_dir}.')


# Define a dictionary to map mall descriptions to addresses
mall_addresses = {
    'Cottonwood Mall': '10000 Cottonwood Park NW, Albuquerque, NM 87114',
    'Coronado Mall': '6600 Menaul Blvd NE, Albuquerque, NM 87110'
}

# Main Code
# Display the header
display_header()

# Instantiate two points
point1 = GeoPoint()
point2 = GeoPoint()

# Set the first point
point1.SetPoint(35.1875, -106.6296)
point1.SetDescription('Cottonwood Mall')
# Set the second point
point2.SetPoint(35.1048, -106.5797)
point2.SetDescription('Coronado Mall')

do_another = 'y'
while do_another == 'y':

    # Ask the user for their location. You can ask for coordinates in three inputs or ask them for their coordinates in one input with each element separated by a coma.
    user_location = input('Enter your location coordinates (latitude, longitude): ').lower()

    # Check if the user separated their coordinates with a comma and if not, prompt the user to do so
    if ',' not in user_location:
        print('Please separate your coordinates with a comma.')
        continue

    # Interim message to make the user feel like the program is doing something
    print('Calculating the distance from your location to each mall...\n')
    time.sleep(1.8)

    # Split the user's input to be separated by a comma
    lat, lon = user_location.split(',')

    # Use point1 and point2's Distance method to find the distance from each point to the user's location
    distance_to_one = point1.Distance(float(lat), float(lon))
    distance_to_two = point2.Distance(float(lat), float(lon))

    # Determine which point is closest to the user
    if distance_to_one < distance_to_two:
        closest_point = point1
    else:
        closest_point = point2

    # Output the result
    display_results(closest_point.GetDescription(), closest_point.GetPoint())

    # Ask if the user wants to do another
    do_another = input('Would you like to see which mall is closer to a different location?? (y/n)? ').lower()

# Pause for 2.5 seconds before the goodbye message
if do_another == 'n':
    time.sleep(2.5)

# Goodbye message
print('\nThank you for using the Which Mall is Closer Calculator.')
gb.Goodbye()
