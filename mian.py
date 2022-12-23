import os
from pytube import YouTube
import requests

URL = input("Enter Video URL : ")

def files(URL):
    r = requests.get(URL)
    with open("testfile.pdf",'wb') as f:
        f.write(r.content)

def video_ditels(URL):
    print("This is a title for your Video : " + YouTube(URL).title)
    print("This is a  channal of Video : " + YouTube(URL).author)
    for i in range(3):
        strem = (str(YouTube(URL).streams.filter(progressive = True)).split(","))
        handel = strem[i].replace('<Stream:', '').replace('[', '').replace('>', '').replace("res=" , "").replace("\"" , "").split()
        print("Reslution of Video : " + handel[2] + "x")
    dorno = input("Do you want to download this video ?                                                       (Y , N) \n")
    if dorno == "Y" or "y":
        res = input("Enter Reslution ..... ?                                              plaes check it on video ditels after you enter \n")
        if "p" not in res:
            doneurl = res + "p"
            download(URL, doneurl)
        else:
            download(URL , res)
    elif dorno == "N" or "n":
        print("ok ................ ;) ")

def download(URL , reslu):
    os.mkdir("Downlaoded")
    YouTube(URL).streams.get_by_resolution(resolution=reslu).download(output_path="Downlaoded\\")
    print("Done>>> </>")

def take_inputs(URL):
    test_link = URL.replace("https:" , "").replace(" " , "").split("/")
    if (("you" and "be") or ("youtube") or ("youtu.be")) in test_link[2]:
        video_ditels(URL)
    else:
        ask = input("it's Youtube Video ?                                                                 (Y , N) \n")
        if ask == "Y":
            video_ditels(URL)
        elif ask == "N":
            files(URL)

take_inputs(URL)