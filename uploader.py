import requests
import os.path

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headears(self):
        return{
            'Content_type' : 'application/json',
            'Authorization' : 'OAuth {}'.format(self.token)
        }

        
    def get_link(self,filename:str):
        ya_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headears()
        folder_path = os.path.basename(filename)
        params = {'path': folder_path, "overwrite": "true"}
        resp = requests.get(ya_link, params=params, headers=headers)
        return resp.json()


    def upload_file(self, filename:str):
        href = self.get_link(filename = filename).get("href","")
        resp = requests.put(href,data = open(filename, 'rb'))
        return resp.status_code

 

if __name__ == '__main__':
    filename = input("path to file u need to upload: ")
    token = input("enter your token: ")
    uploader = YaUploader(token)
    result = uploader.upload_file(filename)
    if result == 201:
        print('ok') 

