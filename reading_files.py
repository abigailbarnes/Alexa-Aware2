import json
import random
import matplotlib.pyplot as plt
import datetime

global file_path

def ambientnoise():
    file_path = '/Users/christopherbarnes/cmsc23400/Alexa-Aware2/AWARE_JSON/ZENTITYAMBIENTNOISE.json'
    with open(file_path) as ambient_noise_json:
        device_usage_data = json.load(ambient_noise_json)

    decibels = []
    frequency = []
    rms = []
    timestamp = []

    for object in device_usage_data:
        decibels.append(object['ZDOUBLE_DECIBELS'])
        frequency.append(object['ZDOUBLE_FREQUENCY'])
        rms.append(object['ZDOUBLE_RMS'])
        #timestamp_in_seconds = object['ZTIMESTAMP']
        #timestamp.append(object['ZTIMESTAMP'])
        timestamp.append(datetime.datetime.fromtimestamp(object['ZTIMESTAMP']/1000.0))
        #print(object['ZTIMESTAMP'])
        #print(datetime.datetime.fromtimestamp(object['ZTIMESTAMP']/1000.0))


    #plotting time vs. decibels
    plt.plot(timestamp, decibels)
    plt.title('Ambient Noise: Time vs. Decibels')
    plt.xlabel('Time')
    plt.ylabel('Decibels (dB)')
    #plt.show()
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/AmbientNoiseDecibels.png')
    plt.clf()

    #plotting time vs. frequency
    plt.plot(timestamp, frequency)
    plt.title('Ambient Noise: Time vs. Frequencies')
    plt.xlabel('Time')
    plt.ylabel('Frequency (Hz)')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/AmbientNoiseFrequency.png')
    plt.clf()

    #plotting time vs. rms
    plt.plot(timestamp, rms)
    plt.title('Ambient Noise: Time vs. Root Mean Square')
    plt.xlabel('Time')
    plt.ylabel('RMS (V)')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/AmbientNoiseRMS.png')
    plt.clf()

def bluetooth():
    file_path = '/Users/christopherbarnes/cmsc23400/Alexa-Aware2/AWARE_JSON/ZENTITYBLUETOOTH.json'
    with open(file_path) as bluetooth_json:
        bluetooth_usage = json.load(bluetooth_json)

    rssi = []
    timestamp = []

    for object in bluetooth_usage:
        rssi.append(object['ZBT_RSSI'])
        timestamp.append(datetime.datetime.fromtimestamp(object['ZTIMESTAMP']/1000.0))


    #plotting time vs. rssi
    plt.plot(timestamp, rssi)
    plt.title('Bluetooth: Time vs. Recieved Singal Strength Indicator')
    plt.xlabel('Time')
    plt.ylabel('RSSI')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/Bluetooth.png')
    plt.clf()

def location():
    file_path = '/Users/christopherbarnes/cmsc23400/Alexa-Aware2/AWARE_JSON/ZENTITYLOCATION.json'
    with open(file_path) as location_json:
        location_usage = json.load(location_json)

    altitude = []
    bearing = []
    latitude = []
    longitude = []
    timestamp = []

    for object in location_usage:
        altitude.append(object['ZDOUBLE_ALTITUDE'])
        bearing.append(object['ZDOUBLE_BEARING'])
        latitude.append(object['ZDOUBLE_LATITUDE'])
        longitude.append(object['ZDOUBLE_LONGITUDE'])
        timestamp.append(datetime.datetime.fromtimestamp(object['ZTIMESTAMP']/1000.0))


    #plotting time vs. altitude
    plt.plot(timestamp, altitude)
    plt.title('Location: Time vs. Altitude')
    plt.xlabel('Time')
    plt.ylabel('Altitude')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/LocationAltitude.png')
    plt.clf()

    #plotting time vs. bearing
    plt.plot(timestamp, bearing)
    plt.title('Location: Time vs. Bearing')
    plt.xlabel('Time')
    plt.ylabel('Bearing')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/LocationBearing.png')
    plt.clf()

    #plotting time vs. latitude
    plt.plot(timestamp, latitude)
    plt.title('Location: Time vs. Latitude')
    plt.xlabel('Time')
    plt.ylabel('Latitude')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/LocationLatitude.png')
    plt.clf()

    #plotting time vs. Longitude
    plt.plot(timestamp, longitude)
    plt.title('Location: Time vs. Longitude')
    plt.xlabel('Time')
    plt.ylabel('Longitude')
    plt.savefig('/Users/christopherbarnes/cmsc23400/Alexa-Aware2/Data_Plots/LocationLongitude.png')
    plt.clf()



def main():
    ambientnoise()
    bluetooth()
    location()

if __name__ == "__main__":
    ambientnoise()
    bluetooth()
    location() 