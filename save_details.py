from pytube import YouTube
def save_details_fun(URL , name):
    full_name = name + "Detiles.text"
    text_d = str(f"title is : {name} \n channal name : {YouTube(URL).author}  \n Discribtion is : {YouTube(URL).description} \n Link for channal is : {YouTube(URL).channel_url}  \n rating is : {YouTube(URL).rating} , Linke for video is : {URL}")
    with open("Downlaoded\\" + full_name , 'wb') as f:
        f.write("{}".format(text_d).encode())




