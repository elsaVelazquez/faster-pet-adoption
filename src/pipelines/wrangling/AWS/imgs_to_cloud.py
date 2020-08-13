import boto3
## TODO elsa why doesn't get_file_names work?
# from pipelines.data_structures import get_file_names
import os


def get_file_names(dir_name):
    '''
    For the given path, get the List of all file names in the directory tree 
    '''
    return os.listdir(dir_name)


def print_s3_contents_boto3(connection):
    '''borrowed from DSI AWS lecture '''
    for bucket in connection.buckets.all():
        for key in bucket.objects.all():
            print(key.key)
            
    
    
if __name__ == '__main__':
    
    #path to where all imgs are stored localy
    dir_str = '../../../../data/img/img_dumps/'
    print(dir_str)
    bucket_name = 'faster-pet-adoption.bucket'
    
    file_names = get_file_names(dir_str)
    print(file_names)
        
    
    print("\nStarted boto3 connection") 
    boto3_connection = boto3.resource('s3')
    print_s3_contents_boto3(boto3_connection)
    s3_client = boto3.client('s3')


    for file_name in file_names:
        local_file = dir_str + file_name

        s3_client.upload_file(local_file, bucket_name, file_name)

        print(f"\nUploaded file {file_name}")
        print_s3_contents_boto3(boto3_connection)

