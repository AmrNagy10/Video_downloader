from pytube import YouTube
def save_details_fun(URL , name):
    full_name = name + "Detiles.text"
    text_d = str(f"title is : {name} \nchannal name : {YouTube(URL).author}  \nDiscribtion is : {YouTube(URL).description} \nLink for channal is : {YouTube(URL).channel_url}  \nrating is : {YouTube(URL).rating} \nLinke for video is : {URL}")
    with open("Downlaoded\\" + full_name , 'wb') as f:
        f.write("{}".format(text_d).encode())




