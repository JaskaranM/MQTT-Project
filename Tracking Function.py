import sqlite3
import geocoder

def get_device_location():
    location = geocoder.ip('me')
    if location.ok:
        return location.latlng
    else:
        return None

def save_location_to_database(latitude, longitude):
    connection = sqlite3.connect('Database')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Bikes (Latitude, Longitude) VALUES (?, ?)", (latitude, longitude))
    connection.commit()
    print("Location data saved successfully.")
    cursor.close()
    connection.close()

def main():
    location = get_device_location()
    if location:
        print("Latitude:", location[0])
        print("Longitude:", location[1])
        save_location_to_database(location[0], location[1])
    else:
        print("Failed to retrieve location.")

if __name__ == "__main__":
    main()
