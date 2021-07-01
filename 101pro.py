import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
        
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)  # Initializing Dropdox
        with open(file_from,'rb') as f: 
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)           
        

def main():
    access_token ='DyYhXSNlR7MAAAAAAAAAAcVgmkO2ZOb8s8W7NzlZ5PnrYR_ttBucoicYz269UEN8'
    transferData = TransferData(access_token)
    file_from = input('Enter the file path to transfer : ')
    file_to = '/Project/'

    transferData.upload_file(file_from,file_to)
    print('File has been moved')


main()
