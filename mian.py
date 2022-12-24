import os
from pytube import YouTube
import requests
import save_details

URL = input("Enter Video URL : ")

def files(URL):
    r = requests.get(URL)
    save_as = input("Save as : ")
    with open(f"Downlaoded\\{save_as}",'wb') as f:
        f.write(r.content)

def video_ditels(URL):
    print("This is a title for your Video : " + YouTube(URL).title)
    print("This is a  channal of Video : " + YouTube(URL).author)
    for i in range(3):
        strem = (str(YouTube(URL).streams.filter(progressive = True)).split(","))
        handel = strem[i].replace('<Stream:', '').replace('[', '').replace('>', '').replace("res=" , "").replace("\"" , "").split()
        print("Reslution of Video : " + handel[2] + "x")
    save_or_not = input("Do you want to Save Details ?                                                      (Y , N) \n")
    if save_or_not == ("Y" or "y"):
        name = YouTube(URL).title
        save_details.save_details_fun(URL , name)
    dorno = input("Do you want to download this video ?                                                       (Y , N) \n")
    if dorno == ("Y" or "y"):
        res = input("Enter Reslution ..... ?                                              plaes check it on video ditels after you enter \n")
        if "p" not in res:
            doneurl = res + "p"
            download(URL, doneurl)
        else:
            download(URL , res)
    elif dorno == ("N" or "n"):
        print("ok ................ ;) ")

def download(URL , reslu):
    YouTube(URL).streams.get_by_resolution(resolution=reslu).download(output_path="Downlaoded\\")
    print("Done...</>")

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

try:
    os.mkdir("Downlaoded")
    take_inputs(URL)
except:
    take_inputs(URL)
    """
    else:
        dorno = input("Do you want to download this video ?                                                       (Y , N) \n")"""