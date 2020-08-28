import boto3
import os

def print_s3_contents_boto3(connection):
    '''borrowed from DSI AWS lecture '''
    for bucket in connection.buckets.all():
        for key in bucket.objects.all():
            print(key.key)
            
#TODO elsa why can't i get this function to work anywhere???
import os


def get_file_names(dir_name):
    '''
    For the given path, get the List of all files in the directory tree 
    '''
    # create a list of file and sub directories 
    # names in the given directory 
    files_list = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for file_n in files_list:
        # Create full path
        full_path = os.path.join(dir_name, file_n)
        # If file_n is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + get_file_names(full_path)
        else:
            all_files.append(full_path)
    print(all_files)                
    return all_files        
    
    
if __name__ == '__main__':
    
    #path to where all imgs are stored localy
    directory_str = '../../../../data/img/img_dumps/'
    print(directory_str)
    bucket_name = 'faster-pet-adoption.bucket'
    
    file_names = get_file_names(directory_str)
    print(file_names)
        
    
    print("\nStarted boto3 connection") 
    boto3_connection = boto3.resource('s3')
    print_s3_contents_boto3(boto3_connection)
    s3_client = boto3.client('s3')


    for file_name in file_names:
        # local_file = directory_str + file_name

        local_file =  file_name

        s3_client.upload_file(local_file, bucket_name, file_name)

        print(f"\nUploaded file {file_name}")
        print_s3_contents_boto3(boto3_connection)

