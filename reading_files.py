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
    command = ["No Devices On", "TV/Computer w/ Netflix & Spotify", "Setup Mode","Resting Device Connected to Internet","Muted Device Plugged In", "Speaking, No Commands","Hey Alexa","Today's Weather","Tomorrow's Weather","Call Dad","Amazon Deals","Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(emf, command, 'o-')
    plt.title('Reading 1: Environment vs. EMF')
    plt.ylabel('Command')
    plt.xlabel('EMF (μT)')
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingAbby1.png")
    plt.savefig(fig_location)
    plt.clf()

def emf_abby2(file_path):
    #Abby's EMF reading averages (3 readings taken each time) 
    #MAAD Lab (6 TVs streaming various things, computers, computer lab on other side of facility, many networked devices)
    emf = [115, 790, 879, 858, 882, 1103, 1242, 1265, 1192, 1154, 1176, 761]
    command = ["TV/Computer in room", "Setup Mode","Resting Device Connected to Internet","Muted Device Plugged In", "Speaking, No Commands","Hey Alexa","Today's Weather","Tomorrow's Weather","Call Dad","Amazon Deals","Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(emf, command, 'o-')
    plt.title('Reading 2: Environment vs. EMF')
    plt.ylabel('Command')
    plt.xlabel('EMF (μT)')
    plt.tight_layout()
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingAbby2.png")
    plt.savefig(fig_location)
    plt.clf()


def emf_christina1(file_path):
    #Christina's EMF
    #from a 3 story apartment building, 2 apartments on each floor on S Woodlawn
    emf = [31, 687, 775, 715, 750, 775, 1026, 1020, 1026, 1022, 975]
    command = ["No Devices On", "Setup Mode","Resting Device Connected to Internet","Muted Device Plugged In", "Speaking, No Commands","Hey Alexa","Today's Weather","Tomorrow's Weather","Amazon Deals","Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(emf, command, 'o-')
    plt.title('Reading 3: Environment vs. EMF')
    plt.ylabel('Command')
    plt.xlabel('EMF (μT)')
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingChristina1.png")
    plt.savefig(fig_location)
    plt.clf()

def emf_christina2(file_path):
    #Christina's EMF
    #from a 3 story apartment building, 2 apartments on each floor on S Woodlawn
    emf = [31, 772, 324, 726, 725, 725, 722, 722, 727, 724, 120]
    command = ["No Devices On", "Resting Device Connected to Internet","Muted Device Plugged In", "Speaking, No Commands","Hey Alexa","Today's Weather","Tomorrow's Weather","Call Dad", "Amazon Deals","Play Music", "Device Unplugged"]

    #plotting environment vs. emf
    plt.plot(emf, command, 'o-')
    plt.title('Reading 4: Environment vs. EMF')
    plt.ylabel('Command')
    plt.xlabel('EMF (μT)')
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingChristina2.png")
    plt.savefig(fig_location)
    plt.clf()

def all_emf(file_path):
    #all the emf values in one plot

    ab1_emf = [33, 857, 786, 887, 999, 1084, 1064, 1030, 1062, 819]
    ab1_command = ["No Devices On", "Resting Device Connected to Internet","Muted Device Plugged In", "Speaking, No Commands","Hey Alexa","Today's Weather","Tomorrow's Weather","Amazon Deals","Play Music", "Device Unplugged"]
    ab2_emf = [0, 879, 858, 882, 1103, 1242, 1265, 1154, 1176, 761]
    ch1_emf = [31, 687, 715, 750, 775, 1026, 1020, 1026, 1022, 975]
    ch2_emf = [31, 772, 324, 726, 725, 725, 722, 727, 724, 120]

    plt.plot(ab1_command, ab1_emf, 'ro-')
    plt.plot(ab1_command, ab2_emf, 'bo-')
    plt.plot(ab1_command, ch1_emf, 'go-')
    plt.plot(ab1_command, ch2_emf, 'yo-')
    plt.title('All Readings: Environment vs. EMF')
    plt.xlabel('Command')
    plt.ylabel('EMF (μT)')
    plt.xticks(rotation = 65)
    plt.tight_layout()
    fig_location = os.path.join(file_path, "Data_Plots/WifiReadingAll.png")
    plt.savefig(fig_location)
    plt.clf()


def main():
    file_path = os.getcwd()
    ambientnoise(file_path)
    bluetooth(file_path)
    location(file_path)
    emf_abby1(file_path)
    emf_abby2(file_path)
    emf_christina1(file_path)
    emf_christina2(file_path)
    all_emf(file_path)

if __name__ == "__main__":
    main()