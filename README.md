# REST-dropbox-store

#### It is the REST-service for storing binary data in Dropbox


_The service have methods GET and PUT. All data is stored in the root as files. For using Dropbox API you should have the token for the account you want to link (you can generate an access token for your own account through the App Console)._

## Get all data
* __GET__ _/dbx-store/api/v1.0/files_

 Return all files

#### Example:
```
$ curl -i http://127.0.0.1:5000/dbx-store/api/v1.0/files
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 342
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Sun, 01 Apr 2018 13:34:47 GMT

{
  "files": [
    {
      "data": "b'010010000110010101101100011011000110111001101111011100100110110001100100\\n'",
      "name": "bin-test"
    },
    {
      "data": "b'0100100001100101011011000110110001101111\\n'",
      "name": "hello"
    }
  ]
}
```
## Get data by key
* __GET__ _/dbx-store/api/v1.0/files/\<name>_

Return contents of the file by key(filename)
  
#### Example:
```
$ curl -i http://127.0.0.1:5000/dbx-store/api/v1.0/files/bin-test
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 123
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Sun, 01 Apr 2018 13:35:40 GMT

{
  "bin-test": "b'010010000110010101101100011011000110111001101111011100100110110001100100\\n'"
}
```
## Edit data
* __PUT__ _/dbx-store/api/v1.0/files/\<name>_

Changes the data of a file by key(filename). If the file file with such <name> did not exist before, it will be created. Also for using PUT method you should have credential. 

By default:  
__USERNAME__: admin   
__PASSWORD__: python

#### Example:
```
$ curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"data":"111101"}' http://127.0.0.1:5000/dbx-store/api/v1.0/files/hello
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 43
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Sun, 01 Apr 2018 13:36:53 GMT

{
  "data": "111101",
  "name": "hello"
}
```
