import json
import random
import matplotlib.pyplot as plt
import datetime
import os

def ambientnoise(file_path):
    ambient_file = os.path.join(file_path, "AWARE_JSON/ZENTITYAMBIENTNOISE.json")
    with open(ambient_file) as ambient_noise_json:
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
    fig_location = os.path.join(file_path, "Data_Plots/AmbientNoiseDecibels.png")

    plt.savefig(fig_location)
    plt.clf()

    #plotting time vs. frequency
    plt.plot(timestamp, frequency)
    plt.title('Ambient Noise: Time vs. Frequencies')
    plt.xlabel('Time')
    plt.ylabel('Frequency (Hz)')
    fig_location = os.path.join(file_path, "Data_Plots/AmbientNoiseFrequency.png")
    plt.savefig(fig_location)
    plt.clf()

    #plotting time vs. rms
    plt.plot(timestamp, rms)
    plt.title('Ambient Noise: Time vs. Root Mean Square')
    plt.xlabel('Time')
    plt.ylabel('RMS (V)')

    fig_location = os.path.join(file_path, "Data_Plots/AmbientNoiseRMS.png")
    plt.savefig(fig_location)
    plt.clf()

def bluetooth(file_path):
    bluetooth_path = os.path.join(file_path, "AWARE_JSON/ZENTITYBLUETOOTH.json")
    with open(bluetooth_path) as bluetooth_json:
        bluetooth_usage = json.load(bluetooth_json)

    rssi = []
    timestamp = []

    for object in bluetooth_usage:
        rssi.append(object['ZBT_RSSI'])
        timestamp.append(datetime.datetime.fromtimestamp(object['ZTIMESTAMP']/1000.0))
        #rssi.append(object['bt_rssi'])
        #timestamp.append(datetime.datetime.fromtimestamp(object['timestamp']/1000.0))


    #plotting time vs. rssi
    plt.plot(timestamp, rssi)
    plt.title('Bluetooth: Time vs. Recieved Singal Strength Indicator')
    plt.xlabel('Time')
    plt.ylabel('RSSI')
    fig_location = os.path.join(file_path, "Data_Plots/Bluetooth.png")
    plt.savefig(fig_location)
    plt.clf()

def location(file_path):
    location_path = os.path.join(file_path, "AWARE_JSON/ZENTITYLOCATION.json")
    with open(location_path) as location_json:
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
    fig_location = os.path.join(file_path, "Data_Plots/LocationAltitude.png")
    plt.savefig(fig_location)
    plt.clf()

    #plotting time vs. bearing
    plt.plot(timestamp, bearing)
    plt.title('Location: Time vs. Bearing')
    plt.xlabel('Time')
    plt.ylabel('Bearing')
    fig_location = os.path.join(file_path, "Data_Plots/LocationBearing.png")
    plt.savefig(fig_location)
    plt.clf()

    #plotting time vs. latitude
    plt.plot(timestamp, latitude)
    plt.title('Location: Time vs. Latitude')
    plt.xlabel('Time')
    plt.ylabel('Latitude')
    fig_location = os.path.join(file_path, "Data_Plots/LocationLatitude.png")
    plt.savefig(fig_location)
    plt.clf()

    #plotting time vs. Longitude
    plt.plot(timestamp, longitude)
    plt.title('Location: Time vs. Longitude')
    plt.xlabel('Time')
    plt.ylabel('Longitude')
    fig_location = os.path.join(file_path, "Data_Plots/LocationLongitude.png")
    plt.savefig(fig_location)
    plt.clf()

def emf_abby1(file_path):
    #Abby's EMF reading averages (3 readings taken each time) 
    #from a 7 story apartment building, 4 apartments on each floor on S Dorchester
    emf = [33, 48, 610, 857, 786, 887, 999, 1084, 1064, 1064, 1030, 1062, 819]
    command = ["No Devices On", "TV and Computer Streaming Netflix and Spotify in Room", "Setup Mode","Resting Device Connected to Internet","Muted Device Plugged In", "Speaking Around Alexa, No Commands","Hey Alexa","Hey Alexa, Tell Me the Weather","Hey Alexa, Tell Me the Weather Tomorrow","Hey Alexa, Call Dad","Hey Alexa, Tell Me the Amazon Deals","Hey Alexa, Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(command, emf)
    plt.title('Wifi Reading 1: Environment vs. EMF')
    plt.xlabel('Command')
    plt.ylabel('EMF (μT)')
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingAbby1.png")
    plt.savefig(fig_location)
    plt.clf()

def emf_christina1(file_path):
    #Christina's EMF
    emf = [31, 293, 687, 775, 715, 750, 775, 1026, 1020, 843, 1026, 1022, 975]
    command = ["No Devices On", "TV and Computer Streaming Netflix and Spotify in Room", "Setup Mode","Resting Device Connected to Internet","Muted Device Plugged In", "Speaking Around Alexa, No Commands","Hey Alexa","Hey Alexa, Tell Me the Weather","Hey Alexa, Tell Me the Weather Tomorrow","Hey Alexa, Call Dad","Hey Alexa, Tell Me the Amazon Deals","Hey Alexa, Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(command, emf)
    plt.title('Wifi Reading 1: Environment vs. EMF')
    plt.xlabel('Command')
    plt.ylabel('EMF (μT)')
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingChristina1.png")
    plt.savefig(fig_location)
    plt.clf()


def main():
    file_path = os.getcwd()
    ambientnoise(file_path)
    bluetooth(file_path)
    location(file_path)
    emf_abby1(file_path)
    emf_christina1(file_path)

if __name__ == "__main__":
    main()