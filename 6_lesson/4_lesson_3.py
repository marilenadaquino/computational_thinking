# import ssl, unicodedata , sys 
# from xmlutils.xml2csv import xml2csv
# converter = xml2csv('Authority-Photographers.xml', "Authority-Photographers.csv", encoding="utf-8")
# converter.convert(tag="ROW")

# install lxml, rquests , BeautifulSoup , fuzz , json
import requests, urllib.parse, urllib, csv, re  # added urllib.parse and json
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz


def reconcileDBPedia(csvfile, fieldname):
    retrievedURIs, truePositive, rows = 0, 0, 0  # counting precision
    baseURL = 'http://lookup.dbpedia.org/api/search/KeywordSearch?MaxHits=1&QueryString='
    # f=csv.writer(open('Authority-Photographers-reconciliation.csv', 'w')) #changed the name of the file, that will be printed not writed in a file
    # f.writerow(['search']+['searchDirectOrder']+['result']+['ratio']+['partialRatio']+['tokenSort']+['tokenSet']+['avg']+['uri'])
    with open(csvfile, encoding='utf-8') as csvfile:  #  added encoding
        reader = csv.DictReader(csvfile)

        for row in reader:
            rows += 1  # for recall
            name = str(row[fieldname])  # changed fieldname
            nameDirect = name.strip()[name.find(',') + 2:] + ' ' + name[:name.find(',')]
            nameEdited = urllib.parse.quote(name.encode('utf-8').strip())  # urllib.parse.quote
            url = baseURL + nameEdited.strip()
            response = requests.get(url).content
            record = BeautifulSoup(response, "lxml").find('html').find('body').find('arrayofresult').find('result')

            try:
                label = record.find('label').text.encode('utf-8')
                uri = record.find('uri').text
                description = record.find('description').text.encode('utf-8')

            except:
                label = ''
                uri = ''
                description = 'no description'

            if name.find(',') != -1:
                ratio = fuzz.ratio(nameDirect, label)
                partialRatio = fuzz.partial_ratio(nameDirect, label)
                tokenSort = fuzz.token_sort_ratio(nameDirect, label)
                tokenSet = fuzz.token_set_ratio(nameDirect, label)
            else:
                ratio = fuzz.ratio(name, label)
                partialRatio = fuzz.partial_ratio(name, label)
                tokenSort = fuzz.token_sort_ratio(name, label)
                tokenSet = fuzz.token_set_ratio(name, label)
                nameDirect = 'N/A'
            avg = (ratio + partialRatio + tokenSort + tokenSet) / 4

            try:
                evidence = record.find(['description', 'label'], text=re.compile('photo')).text.encode('utf-8')
                evidence = 'True'
            except:
                evidence = 'False'

            # distinguish matching URI and not matching
            if uri != '':
                print('matching URI:',
                      [name.strip().encode('utf-8')] + [nameDirect.encode('utf-8')] + [label] + [ratio] + [
                          partialRatio] + [tokenSort] + [tokenSet] + [avg] + [evidence] + [uri] + [description])
                retrievedURIs += 1
                if evidence == 'True':
                    truePositive += 1
            if uri == '':
                print('not matching URI:', [name.strip().encode('utf-8')])

        # calculate precision and recall
        # precision is the number of correct results (truePositive) divided by the number of all returned results (retrievedURIs)
        print('precision:', truePositive / retrievedURIs)
        # recall is the number of correct results (truePositive) divided by the number of results that should have been returned (totalRows)
        print('recall:', truePositive / rows)
reconcileDBPedia('Authority-Photographers.csv', 'AUFN')