import dropbox

class UploadFiles:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6Ry8NaEX4r2Js1JtRqrX7DAAR8P_JdUUtonaeHOWTcFTrdqCHuryrK5PN__MtiRsUPoLuP55sptJkL14ludBvq5jv99YtLSXPqzB2xNQx223ztQcV8QZVmkisyBRcfnGv4SZF4'
    transferData = TransferData(access_token)
    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt' 


    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()