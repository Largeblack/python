# -*- coding: utf-8 -*-
import requests
import urllib
#import bs4
from bs4 import BeautifulSoup
from operator import itemgetter
import psycopg2
import os
# pathname = "butterfly"
# os.makedirs(pathname)
id = ["mono","v_band","h_band","fore_half","3_bands","1_line","lines","vein","grid","eyes","spot","some_spots","spots","complex_wood","edge","stars","block"]
id2 = ["￥xAW?n?o","¯Q?~?n?o"]
url = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:";

url2="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"

# soup = BeautifulSoup(res.text)
#print soup
for tempstr in id:
    res = requests.get("http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:"+tempstr+"&amp;side=display")
    soup = BeautifulSoup(res.content,'html.parser')
    typeval = id.index(tempstr)+1
    print typeval
    url_str = "http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_visual_bi/cgi-bin/browse.pl?new_query=texture:"+tempstr+"&amp;side=display"
    print url_str
    res = requests.get(url_str)
    #print res
    for title in soup.select('table tr td font'):
        a=title.text.split(')')[0]
        Titlea=a
        print a
        b=title.text.split('(')[0]
        #print b
        msg =urllib.quote(b.encode('big5'))
        #print msg
#         print urllib.quote(u'"a"'.encode('big5'))
        urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_keyword/xmlShow.pl?filename="+msg+".xml"
        print urlb
        res2 = requests.get(urlb)
        soup = BeautifulSoup(res2.content,'html.parser')
#         print res2
        for title in soup.select('table tr td font')[5]:#TITLE
            
            #print title.text
            print title.string.split('(')[0]
            Title=title
            for item in soup.select('table tr td font i'):#別名[6]英文名item.string.split('(')[0]
                
                print item.string
                Item=item.string
                
            
                for item1 in soup.select('table tr td font')[8]:#別名內容
                    #print item1
                    Item1=item1
                    for item2 in soup.select('table tr td font')[9]:#生物學分類：
                        #print item2
                        for item3 in soup.select('table tr td font')[10]:#科別
                            #print item3.string
                            Item3=item3.string
        for item4 in soup.select('table tr td font')[12]:#寄主植物：
            #print item4.string
            for item5 in soup.select('table tr td font')[14]:#寄主植物內容
                #print item5.string
                Item5=item5.string
                for item6 in soup.select('table tr td font')[15]:#蜜源植物：
                    #print item6.string
                    for item7 in soup.select('table tr td font')[16]:#蜜源植物內容
                        #print item7.string
                        Item7=item7.string
                        for item8 in soup.select('table tr td font')[17]:#台灣分佈：
                            #print item8.string
                            for item9 in soup.select('table tr td font')[18]:#台灣分佈內容
#                               print item9.string
                                Item9=item9.string
                                for item10 in soup.select('table tr td font')[19]:#其他國家分佈：
                                    #print item10.string
                                    for item11 in soup.select('table tr td font')[20]:#其他國家分佈內容
                                        #print item11.string
                                        Item11=item11.string
                                        for item12 in soup.select('table tr td font')[21]:#備註
                                            #print item12.string
                                            for item13 in soup.select('table tr td font')[22]:#備註
                                                #print item13.string
                                                Item13=item13.string
                                                #卵
#=================================================================================================================================================================
        for itemegg in soup.select('table tr td font')[23]:#卵
            #print itemegg.string
            for item14 in soup.select('table tr td font')[24]:#形狀：
                #print item14.string
                for item15 in soup.select('table tr td font')[25]:#形狀內容   
                    #print item15.string
                    Item15=item15.string   
                    for item16 in soup.select('table tr td font')[26]:#顏色:
                        #print item16.string
                        for item17 in soup.select('table tr td font')[27]:#顏色內容
                            #print item17.string
                            Item17=item17.string
                            for item18 in soup.select('table tr td font')[28]:#大小
                                #print item18.string
                                for item19 in soup.select('table tr td font')[29]:#大小內容
                                    #print item19.string
                                    Item19=item19.string
                                    for item20 in soup.select('table tr td font')[30]:#特徵
                                        #print item20.string
                                        for item21 in soup.select('table tr td font')[31]:#特徵內容
                                            #print item21.string
                                            Item21=item21.string
                                            for item22 in soup.select('table tr td font')[32]:#生長分佈
                                                #print item22.string
                                                for item23 in soup.select('table tr td font')[33]:#生長分佈內容
                                                    #print item23.string
                                                    Item23=item23.string
                                                    for item24 in soup.select('table tr td font')[34]:#天敵
                                                        #print item24.string
                                                        for item25 in soup.select('table tr td font')[35]:#天敵內容
                                                            #print item25.string
                                                            Item25=item25.string
                                                            for item26 in soup.select('table tr td font')[36]:#成長天數：
                                                                #print item26.string
                                                                for item27 in soup.select('table tr td font')[37]:#成長天數內容
                                                                    #print item27.string
                                                                    Item27=item27.string
                                                                    for item28 in soup.select('table tr td font')[38]:#偽裝避敵：
                                                                        #print item28.string
                                                                        for item29 in soup.select('table tr td font')[39]:#偽裝避敵內容
                                                                            #print item29.string
                                                                            Item29=item29.string
                                                                                    #幼蟲
#=================================================================================================================================================================
        for itemlarva in soup.select('table tr td font')[40]:#幼：
            #print itemlarva.string
            for itemlarva1 in soup.select('table tr td font')[41]:#蟲：
                #print itemlarva1.string
                for item30 in soup.select('table tr td font')[42]:#形狀：
                    #print item30.string
                    for item31 in soup.select('table tr td font')[43]:#形狀內容
                        #print item31.string
                        Item31=item31
                        for item32 in soup.select('table tr td font')[44]:#顏色
                            #print item32.string
                            for item33 in soup.select('table tr td font')[45]:#顏色內容
                                #print item33.string
                                Item33=item33
                                for item34 in soup.select('table tr td font')[46]:#大小:
                                    #print item34.string
                                    for item35 in soup.select('table tr td font')[47]:#大小內容
                                        #print item35.string
                                        Item35=item35
                                        for item36 in soup.select('table tr td font')[48]:#特徵:
                                            #print item36.string
                                            for item37 in soup.select('table tr td font')[49]:#特徵內容
                                                #print item37.string
                                                Item37=item37
                                                for item38 in soup.select('table tr td font')[50]:#生長分佈：
                                                    #print item38.string
                                                    for item39 in soup.select('table tr td font')[51]:#生長分佈內容
                                                        #print item39.string
                                                        Item39=item39
                                                        for item40 in soup.select('table tr td font')[52]:#天敵：
                                                            #print item40.string
                                                            for item41 in soup.select('table tr td font')[53]:#天敵內容
                                                                #print item41.string
                                                                Item41=item41
                                                                for item42 in soup.select('table tr td font')[54]:#成長天數
                                                                    #print item42.string
                                                                    for item43 in soup.select('table tr td font')[55]:#成長天數內容
                                                                        #print item43.string
                                                                        Item43=item43
                                                                        for item44 in soup.select('table tr td font')[56]:#偽裝避敵：
                                                                            #print item44.string
                                                                            for item45 in soup.select('table tr td font')[57]:#偽裝避敵內容
                                                                                #print item45.string
                                                                                Item45=item45
                                                                                #蛹
#=================================================================================================================================================================
        for itempupa in soup.select('table tr td font')[58]:#蛹
            #print itempupa.string
            for item46 in soup.select('table tr td font')[59]:#形狀:
                #print item46.string
                for item47 in soup.select('table tr td font')[60]:#形狀內容
                    #print item47.string
                    Item47=item47
                    for item48 in soup.select('table tr td font')[61]:#顏色：
                        #print item48.string
                        for item49 in soup.select('table tr td font')[62]:#顏色內容
                            #print item49.string
                            Item49=item49
                            for item50 in soup.select('table tr td font')[63]:#大小:
                                #print item50.string
                                for item51 in soup.select('table tr td font')[64]:#大小內容
                                    #print item51.string
                                    Item51=item51
                                    for item52 in soup.select('table tr td font')[65]:#特徵
                                        #print item52.string
                                        for item53 in soup.select('table tr td font')[66]:#特徵內容
                                            #print item53.string
                                            Item53=item53
                                            for item54 in soup.select('table tr td font')[67]:#生長分佈
                                                #print item54.string
                                                for item55 in soup.select('table tr td font')[68]:#生長分佈內容
                                                    #print item55.string
                                                    Item55=item55
                                                    for item56 in soup.select('table tr td font')[69]:#天敵：
                                                        #print item56.string
                                                        for item57 in soup.select('table tr td font')[70]:#天敵內容
                                                            #print item57.string
                                                            Item57=item57
                                                            for item58 in soup.select('table tr td font')[71]:#成長天數:
                                                                #print item58.string
                                                                for item59 in soup.select('table tr td font')[72]:#成長天數內容
                                                                    #print item59.string
                                                                    Item59=item59
                                                                    for item60 in soup.select('table tr td font')[73]:#偽裝避敵：
                                                                        #print item60.string
                                                                        for item61 in soup.select('table tr td font')[74]:#偽裝避敵內容
                                                                            #print item61.string
                                                                            Item61=item61
                                                                                #成蟲
#=================================================================================================================================================================
        for iteminsect in soup.select('table tr td font')[75]:#成:
            #print iteminsect.string
            for iteminsect1 in soup.select('table tr td font')[76]:#蟲:
                #print iteminsect1.string
                for item62 in soup.select('table tr td font')[77]:#形狀:
                    #print item62.string
                    for item63 in soup.select('table tr td font')[78]:#形狀內容:
                        #print item63.string
                        Item63=item63.string
                        for item64 in soup.select('table tr td font')[79]:#顏色:
                            #print item64.string
                            for item65 in soup.select('table tr td font')[80]:#顏色內容
                                #print item65.string
                                Item65=item65.string
                                for item66 in soup.select('table tr td font')[81]:#大小
                                    #print item66.string
                                    for item67 in soup.select('table tr td font')[82]:#大小內容
                                        #print item67.string
                                        Item67=item67.string
                                        for item68 in soup.select('table tr td font')[83]:#特徵
                                            #print item68.string
                                            for item69 in soup.select('table tr td font')[84]:#特徵內容
                                                #print item69.string
                                                Item69=item69.string
                                                for item70 in soup.select('table tr td font')[85]:#生長分佈：
                                                    #print item70.string
                                                    for item71 in soup.select('table tr td font')[86]:#生長分佈內容
                                                        #print item71.string
                                                        Item71=item71.string
        for item72 in soup.select('table tr td font')[88]:#天敵
            #print item72
            for item73 in soup.select('table tr td font')[89]:#天敵內容
                #print item73
                Item73=item73.string
                for item74 in soup.select('table tr td font')[90]:#成長天數:
                    #print item74
                    for item75 in soup.select('table tr td font')[91]:#成長天數內容
                        #print item75
                        Item75=item75.string
                        for item76 in soup.select('table tr td font')[92]:#偽裝避敵：
                            #print item76
                            for item77 in soup.select('table tr td font')[93]:#偽裝避敵內容
                                #print item77
                                Item77=item77.string
                                for item78 in soup.select('table tr td font')[94]:#季節
                                    #print item78
                                    for item79 in soup.select('table tr td font')[95]:#季節內容
                                        #print item79
                                        Item79=item79.string
                                        for item80 in soup.select('table tr td font')[96]:#其他生態行為：
                                            #print item80
                                            for item81 in soup.select('table tr td font')[97]:#其他生態行為內容
                                                #print item81
                                                Item81=item81.string
                                                    
#                                                     bfname = url_str+item['src']
#                                                     res2 ='000001'
#                                                     if bfname.find(res2)!=-1:
#                                                         print bfname                                 
#                                     for item6 in soup.select('table tr td font')[15]:#寄主植物
#                                         #print item6.string
                                
#             contOK=content
#             print contOK
            #print content.get('font')
#             for item in soup.select('table tr td font'):#TITLE
#                 print i    tem.text.split('|')[0]
        conn = psycopg2.connect(host='localhost',database='i3stest9' ,user='postgres' ,password='viplab4719')
        cur = conn.cursor()
        #cur.execute("INSERT INTO object(type,cname,ename)VALUES(%s,%s,%s)",(typeval,Titlea,Item,))
        #cur.execute("INSERT INTO Butterfuly(bname,sname,divisions,hostplants,nectarPlants,taiwandistribution,othercountries,remark)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Title,Item1,Item3,Item5,Item7,Item9,Item11,Item13))
        #cur.execute("INSERT INTO larva(shape,color,size,feature,distributed,predators,growthDays,camouflage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Item31,Item33,Item35,Item37,Item39,Item41,Item43,Item45))
        #cur.execute("INSERT INTO pupa(shape,color,size,feature,distributed,predators,growthDays,camouflage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Item47,Item49,Item51,Item53,Item55,Item57,Item59,Item61))
        #cur.execute("INSERT INTO egg(shape,color,size,feature,distributed,predators,growthDays,camouflage)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(Item15,Item17,Item19,Item21,Item23,Item25,Item27,Item29))
        #cur.execute("INSERT INTO Insect(shape,color,size,feature,distributed,predators,growthDays,camouflage,season,othercologicalbehavior)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Item63,Item65,Item67,Item69,Item71,Item73,Item75,Item77,Item79,Item81))
        cur.execute("INSERT INTO url(path)VALUES(%s)",(urlb,))
        #cur.execute("INSERT INTO co(cid)VALUES(%s)",(typeval,))
#         cur.execute("INSERT INTO class(type)VALUES(%s)",(typeval,))
        
        conn.commit()     
        cur.close()
        conn.close()  
        
     
    
# for tempstr in id2:
#     #print res.text
# #     for content in soup.select('center table tr td font a'):
# #         content.get('href')
#         urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/query_keyword/xmlShow.pl?filename="+tempstr+".xml"
# #         urllib.unquote(urlb).decode('utf8') 
#          
#         #print urllib.unquote(urlb).decode('utf8')
#         print urllib.quote(u'台灣鳳蝶'.encode('big5'))
        #urlb="http://turing.csie.ntu.edu.tw/ncnudlm/cgi-bin/"+content.get('href')
        #urlb.replace('/../..','')
        #print urlb 
        #print urlb.strip('../../')
        #urlb=urlb.decode('big5')
#         urlb=urlb.decode('big5').encode('utf-8')
        #print urlb
#         res2 = requests.get(urlb)
#         #print res2
#         for item in soup.select('table tr td font'):
#             #res.encoding = res.apparent_encoding
#             #print res.encoding
#             print item.encode('big5')  
#             if(title.text != ""):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            #print item.text
            