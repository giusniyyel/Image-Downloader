import requests

print("### Welcome to image downloader ###\n")

x = 17578

while x < 17652:

    url = ""+str(x)+".jpg"

    print("Accessing to "+url+"...")

    response = requests.get(url)

    file_directory = "images/part1/"

    file_name = str(x)+".jpg"

    print("Saving file: "+file_name+"...")

    file = open((file_directory+file_name), "wb")

    file.write(response.content)

    file.close()

    print("Image "+file_name+" downloaded!\n")

    x += 1

print("All images downloaded!!")