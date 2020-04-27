from gtts import gTTS 
import tensorflow as tf
import gpt_2_simple as gpt2
import random
import tarfile
import requests
import os

filepath="checkpoint_runscripts.tar"
googefileid= "1qx8pywi7HFirIHgduSU-qKNZqqQ4n8At"

def extract():
    """Copies the checkpoint folder from a mounted Google Drive."""
    with tarfile.open(filepath, 'r') as tar:
        tar.extractall()
    os.remove(filepath)
    print("File",filepath, "Removed!")

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

# download_file_from_google_drive(googefileid,filepath)
# extract()
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='runscripts')

def createStory():
    temp= random.randint(7,9)/10
    print(temp)
    text= gpt2.generate(sess,
            run_name='runscripts',
            length=600,
            temperature=0.85,
            top_p=1,
            top_k=30,
            nsamples=1,
            batch_size=1,
            return_as_list=True
            )
            
    text= text[0]
    return text

def Story():
    text = createStory()
    Story = open(r"Story.txt","w+") 
    Story.write(text)
    print(text)

def MP3():
    fileHandler = open("Story.txt", "r")
    myText =fileHandler.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("Story.mp3")
    fileHandler.close()
    os.system("start Story.mp3")

Story()
MP3()