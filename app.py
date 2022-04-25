from crypt import methods
from flask import Flask, redirect, render_template, request, url_for
import boto3
from botocore.exceptions import ClientError
from Upload import upload_files
from werkzeug.utils import secure_filename




app = Flask(__name__)




@app.route("/create", methods=['GET', 'POST'])
def create():
    alert="8"
    if request.method=='POST':
        Bucket_name=request.form['S3']
        print(Bucket_name)
        try :
            s3= boto3.client('s3')
            s3.create_bucket(Bucket=Bucket_name)
            print("Bucket Created Successfully")
            alert="0"
        except ClientError as e:
            alert="1"
    
        print(alert)
    return render_template("CreateS3.html",alert1=alert)

@app.route("/")
def show():
    s3= boto3.client('s3')
    response=s3.list_buckets()
    print(response['Buckets'])
    return render_template("ShowS3.html", All_Buckets=response['Buckets']);


@app.route("/view/<bucket_name>")
def view(bucket_name):
    Rs3=boto3.resource('s3')
    s3= boto3.client('s3')
    bucket=Rs3.Bucket(name=bucket_name)
    files=list(bucket.objects.all())
    return render_template("files.html",  All_files=files, bn=bucket_name);



@app.route("/Add/<bn>",methods=["POST"])
def upload(bn):
    if request.method =='POST':
        file_name=request.form['file']
        print(file_name)
        print(bn)
        upload_files(file_name,bn)
    return render_template("upload.html");




if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")