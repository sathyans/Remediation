#CSU Proficiency Compiler
#CSUMB IAR

import urllib.request
import re


def cleanup(c):
    cell = str(c)
    cell = cell.replace("b\'","")
    cell = cell.replace("\'","")
    cell = cell.replace("<BR>","")
    cell = cell.replace("<TD>","")
    cell = cell.replace("</TD>","")
    cell = cell.replace("<br>","")
    cell = cell.replace("<td>","")
    cell = cell.replace("</td>","")    
    cell = cell.replace(",","")
    return cell


url1 = "http://www.asd.calstate.edu/remediation/"
url2 = "/Rem_"
url3 = "_fall"
url4 = ".htm"
stopline = 124
fout = open('rem.csv','w')
fout.write('Year of Cohort' +','  + 'Campus' + ',' + 'Cohort' + ',' + 'Need Math Remediation' + ',' + 'Need English Remediation' + '\n')

csu = dict()
years = dict()

csu = ["Sys","Bak","CI","Chi","DH","EB","Fre","Ful","Hum","LA","LB","MA","MB","Nor","Pom","Sac","SB","SD","SF","SJ","SLO","SM","Son","Sta"]
years = ["05","06","07","08","09","10","11"]


for item in range(24):
    campus = csu[item]
    for item2 in range(7):
        directory = years[item2]
        if directory == "06" or directory == "09":
            line_year = 13
            line_campus = 16
            line_cohort = 113
            line_math = 114
            line_english = 116
        elif directory == "05" or directory == "07" or directory == "08" :
            line_year = 12
            line_campus = 15
            line_cohort = 112
            line_math = 113
            line_english = 115   
        elif directory == "10" or directory == "11" :
            line_year = 12
            line_campus = 15
            line_cohort = 120
            line_math = 121
            line_english = 123        
        else:
            line_year = 13
            line_campus = 16
            line_cohort = 113
            line_math = 114
            line_english = 116            
        str_year = "20" + directory
        url_target = url1 + directory + url2 + campus + url3 + str_year + url4
        print(url_target)
        conn = urllib.request.urlopen(url_target)
        for i in range(stopline):
            word = conn.readline()
            word = word.strip()
            if i == line_year:
                year = word
                year  = cleanup(year)
                
                fout.write(str(year) +',')
            if i == line_campus:
                csucampus = word.rstrip()  
                csucampus = cleanup(csucampus)
                
                fout.write(str(csucampus) +',')
            if i == line_cohort:
                cohort = word.lstrip()
                cohort = cleanup(cohort)
                fout.write(str(cohort) +',')
            if i == line_math:
                math = word.lstrip() 
                math = cleanup(math)
                
                fout.write(str(math) +',')
            if i == line_english:
                english = word.lstrip()     
                english = cleanup(english)
                
                fout.write(str(english))
                fout.write('\n')        
fout.close()
print("Done!")