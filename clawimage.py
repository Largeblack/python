# -*- coding: utf-8 -*-
import requests
import urllib
from pip._vendor.distlib._backport import shutil
#import bs4
from bs4 import BeautifulSoup
from operator import itemgetter
import psycopg2
import os
def imagecrawler(imgfilename, plantfilename, url, picturename):
    rx = requests.get(url, stream=True)
    temppath = imgfilename + '/' + plantfilename
    if not(os.path.exists(imgfilename + '/' + plantfilename)):
        os.makedirs(imgfilename + '/' + plantfilename)
    if rx.status_code == 200:
        with open(temppath + '/' + picturename, 'wb') as f:
            rx.raw.decode_content = True
            shutil.copyfileobj(rx.raw, f)
            f.close()
    return temppath
# pathname = "butterfly"
# os.makedirs(pathname)
id = ["mono","v_band","h_band","fore_half","3_bands","1_line","lines","vein","grid","eyes","spot","some_spots","spots","complex_wood","edge","stars","block"]
id2 = ["￥xAW?n?o","¯Q?~?n?o"]
url = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:";

url2="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"
#pathname = "temppath"
# os.makedirs(pathname)
# soup = BeautifulSoup(res.text)
#print soup
for tempstr in id:
    res = requests.get("http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:"+tempstr+"&amp;side=display")
    soup = BeautifulSoup(res.content,'html.parser')
    typeval = id.index(tempstr)+1
    print typeval
    url_str = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:"+tempstr+"&amp;side=display"
    #print url_str.split(':')[2]
    url2=url_str.split(':')[2]
    url3=url2.split(';')[0]
    print url3
    res = requests.get(url_str)
    for content in soup.select('center table tr td font a img'):#img
        #print content.get('src')
        bfname = content['src']
        #print bfname
        res2=requests.get(bfname,stream=True)
        text= bfname.split('/')[6]
        #print text
        filename="imgbutterfly2"
        
#         data = urllib.urlopen(bfname)
#         f = open(pathname+'/' + str(text),'wb')
#         shutil.copyfileobj(res2.raw,f)
#         f.close()
        imagecrawler(filename,url3,bfname,text)

#         
#         conn = psycopg2.connect(host='localhost',database='bigblack' ,user='postgres' ,password='viplab4719')
#         cur = conn.cursor()
#         #cur.execute("INSERT INTO butterfuly(bname,sname,divisions,hostplants,nectarPlants,taiwandistribution,othercountries,remark)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Title,Item1,Item3,Item5,Item7,Item9,Item11,Item13))
#         #cur.execute("INSERT INTO larva(shape,color,size,feature,distributed,predators,growthDays,camouflage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Item31,Item33,Item35,Item37,Item39,Item41,Item43,Item45))
#         #cur.execute("INSERT INTO pupa(shape,color,size,feature,distributed,predators,growthDays,camouflage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Item47,Item49,Item51,Item53,Item55,Item57,Item59,Item61))
#         #cur.execute("INSERT INTO Insect(shape,color,size,feature,distributed,predators,growthDays,camouflage,season,othercologicalbehavior)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Item63,Item65,Item67,Item69,Item71,Item73,Item75,Item77,Item79,Item81))
#         #cur.execute("INSERT INTO url(url)VALUES(%s)",(urlb,))
#         #cur.execute("INSERT INTO co1(cid)VALUES(%s)",(typeval,))
#         cur.execute("INSERT INTO archive(fname,source)VALUES(%s,%s)",(text,bfname))
#               
#         conn.commit()     
#         cur.close()
#         conn.close()          
            
#                           
        
#     for content in soup.select('center table tr td font a'):#img
#         content.get('href')
#         print content
       
                  
#         urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"+content.get('href')
#         #urlb.replace('/../..','')
#         #print urlb 
#         #print urlb.strip('../../')
#         #urlb=urlb.decode('big5')
# #         urlb=urlb.decode('big5').encode('utf-8')
#         print urlb.replace('../../','')
       
        
#         title = content.find('href').text
# #                 cont =''
#         cont = content.text.replace('../../','')
#         print cont.replace('../../','') 
#     try:
#                     
# #                 title =''
#                 title = content.find("../../")
#                
#                  
# #                 cont =''
#                 cont = content.text.replace(title,'')
#                 print cont.replace(title,'') 
# #                 if(cont != "" or cont != "\n"):                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# #                     print cont
#                 contOK= cont.replace(title,'')  
# #                 print content.text
#     except: 
#              
#                 print content.text
    
#                 contOK=content.text
#                 print type(contOK)
#     for item in soup.select('table tr td a'):
#         print item.get('href')
#        print item.get('href')
#            for item in soup.select('td a'):
#              print item.get('href')
#     for item in soup.select('table tr td table tr td a'):
#             text = item.get('onclick')
            
#         print text.split('myTexture')[1]
#             if text.find("myTexture='")!= -1 :
#                 print text.split('myTexture=')[1]

        
#             print item.split('myTexture')
        #print item.attr('myTexture')
        
        
#         
# -*- coding: utf-8 -*-
# import requests
# import urllib
# #import bs4
# from bs4 import BeautifulSoup
# from operator import itemgetter
# import psycopg2
# id = ["mono"]
# id2 = ["￥xAW?n?o","¯Q?~?n?o"]
# url = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:";
# 
# url2="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"
# 
# # soup = BeautifulSoup(res.text)
# #print soup
# for tempstr in id:
#     res = requests.get("http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_keyword/xmlShow.pl?filename=%AFQ%BE~%BB%F1%BD%BA.xml")
#     soup = BeautifulSoup(res.content,'html.parser')
# #     url_str = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_keyword/xmlShow.pl?filename=%AFQ%BE~%BB%F1%BD%BA.xml"
# #     print url_str
#  
# #     res = requests.get(url_str)
# #     #print res
# #     for title in soup.select('table tr td font'):
# # #         a=title.text.split(')')[-2]
# # #         print a
# #         b=title.text.split('(')[0]
# #         #print b
# #         msg =urllib.quote(b.encode('big5'))
# #         #print msg
# # #         print urllib.quote(u'"a"'.encode('big5'))
# #         urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_keyword/xmlShow.pl?filename="+msg+".xml"
# #         print urlb
# #         res2 = requests.get(urlb)z
# #         soup = BeautifulSoup(res2.content,'html.parser')
# # #         print res2
#     for content in soup.select('table',{'div':'font'}):#TITLE
#              
#             #print content.text
#              
# #             content.text.split('|')[0]
#         contOK=content.text
#         print contOK
# #                   
# #         urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"+content.get('href')
# #         #urlb.replace('/../..','')
# #         #print urlb 
# #         #print urlb.strip('../../')
# #         #urlb=urlb.decode('big5')
# # #         urlb=urlb.decode('big5').encode('utf-8')
# #         print urlb.replace('../../','')
#        
#         
# #         title = content.find('href').text
# # #                 cont =''
# #         cont = content.text.replace('../../','')
# #         print cont.replace('../../','') 
# #     try:
# #                     
# # #                 title =''
# #                 title = content.find("../../")
# #                
# #                  
# # #                 cont =''
# #                 cont = content.text.replace(title,'')
# #                 print cont.replace(title,'') 
# # #                 if(cont != "" or cont != "\n"):                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# # #                     print cont
# #                 contOK= cont.replace(title,'')  
# # #                 print content.text
# #     except: 
# #              
# #                 print content.text
#     
# #                 contOK=content.text
# #                 print type(contOK)
# #     for item in soup.select('table tr td a'):
# #         print item.get('href')
# #        print item.get('href')
# #            for item in soup.select('td a'):
# #              print item.get('href')
# #     for item in soup.select('table tr td table tr td a'):
# #             text = item.get('onclick')
#             
# #         print text.split('myTexture')[1]
# #             if text.find("myTexture='")!= -1 :
# #                 print text.split('myTexture=')[1]
# 
#         
# #             print item.split('myTexture')
#         #print item.attr('myTexture')
#         
#         
# #         
# # #         http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/similar.pl?query=0526.jpg
# # #         http://turing.csie.ntu.edu.tw/ncnudlm/query_visual_bi/dl_data/0298.jpg
# #<td><font size="2">¥Õ§À¶Â½®½º(¶¯)<br/><a href="../../query_keyword/xmlShow.pl?filename=¥Õ§À¶Â½®½º.xml" target="_top"><img border="0" src="http://turing.csie.ntu.edu.tw/ncnudlm/query_visual_bi/dl_data/0554.jpg" width="100"/><br/></a><a href="similar.pl?query=0554.jpg" target="_top">»P¦¹¬Û¦ü¤§¸ê®Æ</a></font></td>