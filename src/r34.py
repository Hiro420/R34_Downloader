from bs4 import *
import requests
import os
import subprocess

# CREATE FOLDER
def folder_create(images):
    try:
        folder_name = input("Enter Folder Name:- ")
        # folder creation
        command = fr"mkdir .\..\{''}"+f"{folder_name}"
        subprocess.run(command, shell=True, capture_output=True)
        newfolder = f"../{folder_name}"

    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name, saving there...")

    # image downloading start
    newfolder = f"../{folder_name}"
    download_images(images, newfolder)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

            # 1.data-srcset
            # 2.data-src
            # 3.data-fallback-src
            # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{page}{i + 1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


# MAIN FUNCTION START
def main(url):
    # content of URL
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    folder_create(images)


# take url
shit = input("Enter Tag:")
page = input("Enter Page Number:")
page2 = int(page) * 21
if page2 == 21:
    page2 = ""
else:
    page2 = "&pid=" + f"{page2}"
if shit == "Albedo" or shit == "Amber" or shit == "Barbara" or shit == "Beidou" or shit == "Collei" or shit == "Diona" or shit == "Dori" or shit == "Eula" or shit == "Fischl" or shit == "Ganyu" or shit == "Hu_Tao" or shit == "Jean" or shit == "Keqing" or shit == "Klee" or shit == "Layla" or shit == "Lisa" or shit == "Mona" or shit == "Nahida" or shit == "Nilou" or shit == "Ningguang" or shit == "Noelle" or shit == "Qiqi" or shit == "Rosaria" or shit == "Sayu" or shit == "Shenhe" or shit == "Sucrose" or shit == "Lumine" or shit == "Venti" or shit == "Xiangling" or shit == "Xinyan" or shit == "Yanfei" or shit == "Yelan" or shit == "Yoimiya" or shit == "Yun_Jin" or shit == "albedo" or shit == "amber" or shit == "barbara" or shit == "beidou" or shit == "collei" or shit == "diona" or shit == "dori" or shit == "eula" or shit == "fischl" or shit == "ganyu" or shit == "hu_tao" or shit == "jean" or shit == "keqing" or shit == "klee" or shit == "layla" or shit == "lisa" or shit == "mona" or shit == "nahida" or shit == "nilou" or shit == "ningguang" or shit == "noelle" or shit == "qiqi" or shit == "rosaria" or shit == "sayu" or shit == "shenhe" or shit == "sucrose" or shit == "lumine" or shit == "venti" or shit == "xiangling" or shit == "xinyan" or shit == "yanfei" or shit == "yelan" or shit == "yoimiya" or shit == "yun_jin" or shit == "Albedo" or shit == "Amber" or shit == "Barbara" or shit == "Beidou" or shit == "Collei" or shit == "Diona" or shit == "Dori" or shit == "Eula" or shit == "Fischl" or shit == "Ganyu" or shit == "Hu Tao" or shit == "Jean" or shit == "Keqing" or shit == "Klee" or shit == "Layla" or shit == "Lisa" or shit == "Mona" or shit == "Nahida" or shit == "Nilou" or shit == "Ningguang" or shit == "Noelle" or shit == "Qiqi" or shit == "Rosaria" or shit == "Sayu" or shit == "Shenhe" or shit == "Sucrose" or shit == "Lumine" or shit == "Venti" or shit == "Xiangling" or shit == "Xinyan" or shit == "Yanfei" or shit == "Yelan" or shit == "Yoimiya" or shit == "Yun Jin" or shit == "albedo" or shit == "amber" or shit == "barbara" or shit == "beidou" or shit == "collei" or shit == "diona" or shit == "dori" or shit == "eula" or shit == "fischl" or shit == "ganyu" or shit == "hu tao" or shit == "jean" or shit == "keqing" or shit == "klee" or shit == "layla" or shit == "lisa" or shit == "mona" or shit == "nahida" or shit == "nilou" or shit == "ningguang" or shit == "noelle" or shit == "qiqi" or shit == "rosaria" or shit == "sayu" or shit == "shenhe" or shit == "sucrose" or shit == "lumine" or shit == "venti" or shit == "xiangling" or shit == "xinyan" or shit == "yanfei" or shit == "yelan" or shit == "yoimiya" or shit == "yun jin":
    shit = shit.replace(r" ", "_")
    url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + f'{shit}' + "_%28" + "genshin_impact%29+" + page2
else:
    shit = shit.replace(r" ", "_")
    url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + f'{shit}' + page2
print(f"{url}")

# CALL MAIN FUNCTION
main(url)