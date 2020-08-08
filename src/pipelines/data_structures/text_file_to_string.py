file = open("pipeline_test_data_2_copy.txt")

def text_file_to_string(file):
    stop_beginning = "{\"animals\":["
    line = file.read().replace("\n", " ").replace(stop_beginning, '')
    stop_end = "\"}}}}"
    if line.endswith(stop_end):
        line = line[:-166]
    file.close()

    print(line)

text_file_to_string(file)