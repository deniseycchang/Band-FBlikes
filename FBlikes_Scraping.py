import requests
import re
from bs4 import BeautifulSoup
import os, csv

script_dir = os.path.dirname(__file__) # abs path of script

fname = 'Band_debutYr'
abspath_debut = script_dir + '/' + fname + '.csv'

fname2 = 'FBlikes'
abspath_fblikes = script_dir + '/' + fname2 + '.csv'
fblikes = open(abspath_fblikes, 'w')

Bds = []
with open(abspath_debut) as csv_year: # reading bands and debut years
    csvReader = csv.reader(csv_year)
    for row in csvReader:
        Bds.append(row)
        
csv_year.close()

for i in Bds:
    gweb = i[0].replace(" ", "")  # remove space
    gweb = gweb.replace("/", "")  # remove /
    gweb = "https://www.facebook.com/" + gweb + "/"  # band facebook fan page
    
    
    r = requests.get(gweb)
    html_doc = r.text    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    div_st = soup.select("div") # collect contents in <div>    
    result = []
    for ss in div_st:
        result.append(str(ss))  # covert contents to str
        
    Gen = []
    for ss in result:
        if (ss.find("people like") >0): # key words to find # of likes
            Gen = ss
            break
        
    Loc_sb = [m.start() for m in re.finditer('people like this', Gen)]

    N_likes = Gen[Loc_sb[0]-11:Loc_sb[0]-1] # number of facebook likes

    N_likes = N_likes.replace(",", "")
    print(i[0], i[1], N_likes)
    
    w = csv.writer(fblikes)
    w.writerow([i[0], i[1], int(N_likes)])


fblikes.close()