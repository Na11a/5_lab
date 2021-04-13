import re

log_file_input = "apache_logs"
log_file_output = "apache_logs_result"
test_text = '83.149.9.216 - - [17/May/2015:11:42:43 +0000] "GET /presentations/logstash-monitorama-2013/images/sad-medic.png HTTP/1.1" 200 430406 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'

input_text = open(log_file_input,'r')
time_true = [("07:40:06"),("13:43:28")]
count = 0 
# :[0][89]:\d+\d+|:[1][012]:\d+\d+|
# :07:\[56]d\d+|07\40\0[6789]|
# :07:\41\d+|
# :13:\[0123]d\d+|:13\4[012]\d+|
# :13:\43\[12]d|
# :13:\43\2[0-8]|
# :13:43:2[0-8]|:13:43:[12]\d|:13:\[0123]\d\d+|:13:4[012]\d+|:07:41\d+|:07:\[56]\d\d+|07:40:[0][6789]|:[0][89]:\d+\d+|:[1][012]:\d+\d+|
for line in input_text:
    date_true = re.findall(r":13:43:2[0-8]|:13:43:[12]\d|:13:[0-3]\d:\d+|:13:4[0-2]:\d+|:07:41:\d+|:07:\[56]\d:\d+|07:40:[0][6-9]|:[0][89]:\d+:\d+|:[1][012]:\d+:\d+",line)
    if date_true:
        get_true = re.findall(r'"GET [\w\W]*?" [2-3]\d+',line)
        if get_true:
            no_images = re.findall(r'png|jpeg|gif|jpg',line)
            if no_images:
                count+=1
                continue
        print(line)
print("Number of right lines = ", count)        