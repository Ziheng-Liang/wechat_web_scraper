## translate.py
import sys, json, numpy as np
from textblob.blob import TextBlob
# from engines import content_engine
import csv

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array: [title, author, date, content] from read_in()
    lines = read_in()
    title = lines[0]
    author = lines[1]
    date = lines[2]
    chinese_blob = TextBlob(lines[3])
    en_content = chinese_blob.translate(from_lang="zh-CN", to='en')
    print en_content # print translated result to web console.

    with open('ada-content-en.csv', r) as source:
        reader = csv.DictReader(source.read().splitlines())
        print "number of row: " + len(reader)

    #combine translated result with ada-content-en.csv to produce new csv.
    #note that csv has fields of: [id,title,author,date,content].
    # newrow = [title, author, date, en_content]
    # with open(r'name', 'a') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(fields)

    ### predicting part, data_url: "ada-content-en.csv"
    # item = request.data.get('item')
    # num_predictions = request.data.get('num', 10)
    # data_url = request.data.get('data-url', None)
    # if not item:
    #     return []
    # return content_engine.predict(str(item), num_predictions, data_url)
    

    ### training part
    # data_url = request.data.get('data-url', None)
    # content_engine.train(data_url)
    # return {"message": "Success!", "success": 1}


#start process
if __name__ == '__main__':
    main()