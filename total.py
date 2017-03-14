# encoding: UTF-8
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import coint
import time, datetime
import MySQLdb
import csv


class dataana(object):
    def __init__(self, symbol1, symbol2, begtime, endtime):
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.begtime = begtime
        self.endtime = endtime
        self.anatime()
        conn = MySQLdb.connect('192.168.0.80', 'root', '123456', 'test')
        cursor = conn.cursor()
        selecttime = str(datetime.datetime.strptime(self.begtime, '%Y-%m-%d %H:%M:%S.%f') - datetime.timedelta(seconds=20))
        begsql1 = "select * from test where contract='%s' and sqltime between '%s' and '%s'" % (self.symbol1, selecttime, self.endtime)
        begsql2 = "select * from test where contract='%s' and sqltime between '%s' and '%s'" % (self.symbol2, selecttime, self.endtime)
        cursor.execute(begsql1)
        a = cursor.fetchall()
        cursor.execute(begsql2)
        b = cursor.fetchall()
        conn.close()
        # begtm0 = datetime.datetime.strptime(time.strftime('%Y-3-8 09:20:00.0',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S.%f')
        self.for_endtime = datetime.datetime.strptime(self.endtime, '%Y-%m-%d %H:%M:%S.%f')
        self.for_begtime = datetime.datetime.strptime(self.begtime, '%Y-%m-%d %H:%M:%S.%f')
        timediff = self.for_endtime - self.for_begtime
        begtm0 = datetime.datetime.strptime(self.begtime, '%Y-%m-%d %H:%M:%S.%f')
        for j in range(len(a)):
            if datetime.datetime.strptime(a[j][11], '%Y-%m-%d %H:%M:%S.%f') >= begtm0:
                break
        for k in range(len(b)):
            if datetime.datetime.strptime(b[k][11], '%Y-%m-%d %H:%M:%S.%f') >= begtm0:
                break
        i = 0
        # j = 0
        # k = 0
        # c=()
        last1 = []
        last2 = []
        buy1 = []
        buy2 = []
        sell1 = []
        sell2 = []
        buylist = []
        selllist = []
        lastlist = []
        while i != timediff.seconds * 2 + 1:
            d = datetime.datetime.strptime(a[j][11], '%Y-%m-%d %H:%M:%S.%f')
            e = datetime.datetime.strptime(b[k][11], '%Y-%m-%d %H:%M:%S.%f')
            if begtm0 == d and begtm0 == e:
                # tup = ((str(begtm0),symbol1+'-'+symbol2,a[j][4] - b[k][4]),)
                # c = c + tup
                last1.append(float(a[j][3]))
                buy1.append(float(a[j][4]))
                sell1.append(float(a[j][5]))
                last2.append(float(b[k][3]))
                buy2.append(float(b[k][4]))
                sell2.append(float(b[k][5]))
                lastlist.append(float(a[j][3] - b[k][3]))
                buylist.append(float(a[j][4] - b[k][4]))
                selllist.append(float(a[j][5] - b[k][5]))
                begtm0 = begtm0 + datetime.timedelta(seconds=0.5)
                i = i + 1
                if len(a) - j != 1:
                    j = j + 1
                if len(b) - k != 1:
                    k = k + 1
                continue
            if begtm0 == d and begtm0 != e:
                # tup = ((str(begtm0), symbol1+'-'+symbol2,a[j][4] - b[k - 1][4]),)
                # c = c + tup
                last1.append(float(a[j][3]))
                buy1.append(float(a[j][4]))
                sell1.append(float(a[j][5]))
                last2.append(float(b[k - 1][3]))
                buy2.append(float(b[k - 1][4]))
                sell2.append(float(b[k - 1][5]))
                lastlist.append(float(a[j][3] - b[k - 1][3]))
                buylist.append(float(a[j][4] - b[k - 1][4]))
                selllist.append(float(a[j][5] - b[k - 1][5]))
                begtm0 = begtm0 + datetime.timedelta(seconds=0.5)
                i = i + 1
                if len(a) - j != 1:
                    j = j + 1
                continue
            if begtm0 != d and begtm0 == e:
                # tup = ((str(begtm0), symbol1+'-'+symbol2,a[j - 1][4] - b[k][4]),)
                # c = c + tup
                last1.append(float(a[j - 1][3]))
                buy1.append(float(a[j - 1][4]))
                sell1.append(float(a[j - 1][5]))
                last2.append(float(b[k][3]))
                buy2.append(float(b[k][4]))
                sell2.append(float(b[k][5]))
                lastlist.append(float(a[j - 1][3] - b[k][3]))
                buylist.append(float(a[j - 1][4] - b[k][4]))
                selllist.append(float(a[j - 1][5] - b[k][5]))
                begtm0 = begtm0 + datetime.timedelta(seconds=0.5)
                i = i + 1
                if len(b) - k != 1:
                    k = k + 1
                continue
            if begtm0 != d and begtm0 != e:
                # tup = ((str(begtm0), symbol1+'-'+symbol2,a[j - 1][4] - b[k - 1][4]),)
                last1.append(float(a[j - 1][3]))
                buy1.append(float(a[j - 1][4]))
                sell1.append(float(a[j - 1][5]))
                last2.append(float(b[k - 1][3]))
                buy2.append(float(b[k - 1][4]))
                sell2.append(float(b[k - 1][5]))
                lastlist.append(float(a[j - 1][3] - b[k - 1][3]))
                buylist.append(float(a[j - 1][4] - b[k - 1][4]))
                selllist.append(float(a[j - 1][5] - b[k - 1][5]))
                # c = c + tup
                begtm0 = begtm0 + datetime.timedelta(seconds=0.5)
                i = i + 1
                continue
        self.lastdes = pd.Series(lastlist).describe()
        self.buydes = pd.Series(buylist).describe()
        self.selldes = pd.Series(selllist).describe()
        self.lastcorrcoef = np.corrcoef(last1, last2)[1, 0]
        self.buycorrcoef = np.corrcoef(buy1, buy2)[1, 0]
        self.sellcorrcoef = np.corrcoef(sell1, sell2)[1, 0]
        self.lastpvalue = coint(last1, last2)[1]
        self.buypvalue = coint(buy1, buy2)[1]
        self.sellpvalue = coint(sell1, sell2)[1]
        self.lastmode = pd.Series(lastlist).mode()[0]
        self.buymode = pd.Series(buylist).mode()[0]
        self.sellmode = pd.Series(selllist).mode()[0]

    def tocsv(self):
        index = ['price', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'mode', 'corrcoef', 'pvalue']
        name = self.symbol1 + '-' + self.symbol2 + ' ' + self.for_begtime.strftime("%H%M") + '~' + self.for_endtime.strftime("%H%M") + '.csv'
        errorFile = open(name, 'wb')
        writeCSV = csv.writer(errorFile)
        finlast = ['last'] + self.lastdes.tolist() + [self.lastmode] + [self.lastcorrcoef] + [self.lastpvalue]
        finbuy = ['buy'] + self.buydes.tolist() + [self.buymode] + [self.buycorrcoef] + [self.buypvalue]
        finsell = ['sell'] + self.selldes.tolist() + [self.sellmode] + [self.sellcorrcoef] + [self.sellpvalue]
        writeCSV.writerow(index)
        writeCSV.writerow(finsell)
        writeCSV.writerow(index)
        writeCSV.writerow(finlast)
        writeCSV.writerow(index)
        writeCSV.writerow(finbuy)
        errorFile.close()
    def anatime(self):
        if self.begtime[11:22] == '09:00:00.0':
            self.begtime = self.begtime[0:11] + '09:00:01.0'
            print "开始时间修正为09点01秒"
    def show(self):
        print "合约:", self.symbol1 + '-' + self.symbol2
        print "分析时间段:", self.begtime + '~~' + self.endtime
        print "卖一:", self.selldes
        print "sellmode", self.sellmode
        print "卖一相关度:", self.sellcorrcoef
        print "卖一P值:", self.sellpvalue
        print "价差", self.lastdes
        print "lastmode", self.lastmode
        print "相关度:", self.lastcorrcoef
        print "P值:", self.lastpvalue
        print "买一:", self.buydes
        print "buymode", self.buymode
        print "买一相关度:", self.buycorrcoef
        print "买一P值:", self.buypvalue
        
        
x = dataana('ag1706', 'ag1712', '2017-03-09 14:10:00.0', '2017-03-09 14:25:00.0')
time.sleep(900)
x.show()
