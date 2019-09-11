# There is an API (http://api.open-notify.org/) that provides information on the 
# International Space Station. 
# Documentation is provided via the website, along with sample request/response.
# Implement a Python script that will accept the following command line arguments, 
# along with any required information, and print the expected results


#CODE STARTS HERE

#importing useful packages
import json
import urllib.request as urb

def where():
    # print the current location of the ISS
    # Example: “The ISS current location at {time} is {LAT, LONG}”
    req = urb.Request("http://api.open-notify.org/iss-now.json")

    response = urb.urlopen(req)

    read = json.loads(response.read())
    print(f"The ISS current location at time: {read['timestamp']} \nThe location lat: {read['iss_position']['latitude']}\nThe location long: {read['iss_position']['longitude']}") 




def passing():
    # print the passing details of the ISS for a given location
    # Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

    # Wilmington DE LAT = 39.745947 LONG = -75.546589
    req2 = urb.Request("http://api.open-notify.org/iss-pass.json?lat=39.745947&lon=-75.546589")

    response2 = urb.urlopen(req2)

    read2 =json.loads(response2.read())

    #two empty lists to hold the duration and time of overhead
    duration = []
    time = []
    for i in range(len(read2['response'])):
        duration.append(read2['response'][i]['duration'])
        time.append(read2['response'][i]['risetime'])


    print(f"The ISS will be overhead (lat:{read2['request']['latitude']} , long: {read2['request']['longitude']})")
    print(f"The ISS will pass this location {read2['request']['passes']} times.")

    for x in range(len(duration)):
        print(f"Duration: {duration[x]} Time: {time[x]}")





# people
# for each craft print the details of those people that are currently in space
def astro():
    req3 = urb.Request("http://api.open-notify.org/astros.json")

    response3 = urb.urlopen(req3)

    read3 = json.loads(response3.read())

    #make 2 empty lists to hold the names of the people and the craft then iterate 
    people = []
    craft = []
    for x in range(len(read3['people'])):
        craft.append(read3['people'][x]['craft'])
        people.append(read3['people'][x]['name'])

    print(f"Number of people in space: {read3['number']}")

    for i in range(len(people)):
        print(f'Name: {people[i]} is at {craft[i]}')


def main():
    #call the functions
    where()
    passing()
    astro()


main()