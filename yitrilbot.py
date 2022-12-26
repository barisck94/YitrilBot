# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:54:35 2021

@author: baris
"""

from binance.client import Client
import talib
import numpy as np
import keys
import datetime
import time
import math
from progress.bar import ShadyBar
import os
import pickle

def indicators1d(sym):
    while 1:
        try:
            d=dict()
            client = Client(keys.api_key, keys.api_secret)
            klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_1DAY, "71 days ago UTC", "now UTC")
            ticker = client.get_orderbook_ticker(symbol=sym)
            d["ticker"] = ticker
            d["klines"] = klines
            klines_close = []
            for i in range(67):
                klines_close.append(float(klines[-67+i][4]))
            closearray = np.asarray(klines_close, dtype = None, order = None)
            rsi = talib.RSI(closearray, 13)
            fastk, fastd = talib.STOCH(rsi, rsi, rsi,fastk_period=16,slowk_period=6,slowd_period=3)
            d["fastk"] = fastk
            d["fastd"] = fastd
            return d
        except:
            pass
        
def indicators1h(sym):
    while 1:
        try:
            d=dict()
            client = Client(keys.api_key, keys.api_secret)
            klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_1HOUR, "71 hours ago UTC", "now UTC")
            ticker = client.get_orderbook_ticker(symbol=sym)
            d["ticker"] = ticker
            d["klines"] = klines
            klines_close = []
            for i in range(67):
                klines_close.append(float(klines[-67+i][4]))
            closearray = np.asarray(klines_close, dtype = None, order = None)
            rsi = talib.RSI(closearray, 13)
            fastk, fastd = talib.STOCH(rsi, rsi, rsi,fastk_period=16,slowk_period=6,slowd_period=3)
            d["fastk"] = fastk
            d["fastd"] = fastd
            return d
        except:
            pass
        
def indicators4h(sym):
    while 1:
        try:
            d=dict()
            client = Client(keys.api_key, keys.api_secret)
            klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_4HOUR, "273 hours ago UTC", "now UTC")
            ticker = client.get_orderbook_ticker(symbol=sym)
            d["ticker"] = ticker
            d["klines"] = klines
            klines_close = []
            for i in range(67):
                klines_close.append(float(klines[-67+i][4]))
            closearray = np.asarray(klines_close, dtype = None, order = None)
            rsi = talib.RSI(closearray, 13)
            fastk, fastd = talib.STOCH(rsi, rsi, rsi,fastk_period=16,slowk_period=6,slowd_period=3)
            d["fastk"] = fastk
            d["fastd"] = fastd
            return d
        except:
            pass
        
def buy(sym,bought_qty,denominator):
    while 1:
        try:
            client = Client(keys.api_key, keys.api_secret)
            balance_USDT = float(client.get_asset_balance(asset="USDT")["free"])
            if balance_USDT > 10:
                order_amount = float( "{0:.4g}".format((float(balance_USDT)-0.1)/(denominator-bought_qty) ))
                order = client.order_market_buy(
                    symbol=sym,
                    quoteOrderQty=order_amount)
                print("\n**********************\n",order["origQty"]," ",sym," alındı", datetime.datetime.now().strftime("%H:%M:%S"),"**********************\n")
            else:
                print("USDT yok?", datetime.datetime.now().strftime("%H:%M:%S"))
            return order
            break
        except:
            print("except buy",sym)
            return order
            break
    
def sell(sym):
    while 1:
        try:
            client = Client(keys.api_key, keys.api_secret)
            balance_coin = float(client.get_asset_balance(asset=(sym[:-4]))["free"])
            if balance_coin != 0:
                order = client.order_market_sell(
                    symbol=sym,
                    quantity=balance_coin)
                assetUSDT = client.get_asset_balance(asset='USDT')
                print("\n**********************\n","satıldı. dolar: ",assetUSDT," ",  datetime.datetime.now().strftime("%H:%M:%S"),"**********************\n")
                return order
            else:
                print("coin yok?", datetime.datetime.now().strftime("%H:%M:%S"))
                break
        except:
            print("except sell",sym)
            break
        
os.system('cls' if os.name == 'nt' else 'clear')  
liste = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'TOMOUSDT', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT', 'WTCUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', 'GXSUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'REPUSDT', 'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT', 'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT', 'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT', 'ALPHAUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT', 'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT', 'STRAXUSDT', 'UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'REEFUSDT', 'OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT', 'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT', 'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT', 'ALICEUSDT', 'LINAUSDT', 'PERPUSDT', 'RAMPUSDT', 'CFXUSDT', 'EPSUSDT', 'AUTOUSDT', 'TKOUSDT', 'PUNDIXUSDT', 'TLMUSDT', 'BTGUSDT', 'MIRUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT', 'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT', 'NUUSDT', 'XVGUSDT', 'ATAUSDT', 'GTCUSDT', 'TORNUSDT', 'KEEPUSDT']
pozisyonlar_kabul = [0,1,2,3,4]
interface, interface2, interface3 = "","",""
satin_liste = []
canli_havuz = []
denominator = 4
pos = [0] * len(liste)
os.system('cls' if os.name == 'nt' else 'clear')
while 1:
    in1 = input("...\n")
    commnd = in1.split(" ")
    try:
        if commnd[0] == "start":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif commnd[0] == "pos":
            try:
                commnd[1] = int(commnd[1])
            except:
                commnd[1] = liste.index(commnd[1])
            os.system('cls' if os.name == 'nt' else 'clear')  
            print(liste[int(commnd[1])]," ",pos[int(commnd[1])])
            in2 = input("\ndeğiştirilecek pozisyon?\n 0 = çıkışta, kontrol dışı\n 1 = düşüşte\n 2 = çıkışa başladı\n 3 = satın alındı\n ")
            pos[int(commnd[1])] = int(in2)
        elif commnd[0] == "pop":
            try:
                commnd[1] = int(commnd[1])
            except:
                commnd[1] = liste.index(commnd[1])
                
            os.system('cls' if os.name == 'nt' else 'clear')
            print(liste[commnd[1]],"listeden silindi.\n")
            liste.pop(int(commnd[1]))
            pos.pop(int(commnd[1]))
        elif commnd[0] == "save":
            open_file = open("liste.dat", "wb")
            pickle.dump(liste, open_file)
            open_file.close()
            open_file = open("pos.dat", "wb")
            pickle.dump(pos, open_file)
            open_file.close()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("save başarılı.")
        elif commnd[0] == "load":
            try:
                open_file = open("pos.dat", "rb")
                pos = pickle.load(open_file)
                open_file.close()
                print("pozisyonlar yüklendi")
                time.sleep(0.5)
            except:
                print("pozisyon kayıt dosyası bulunamadı...")
                time.sleep(3)
            try:
                open_file = open("liste.dat", "rb")
                liste = pickle.load(open_file)
                open_file.close()
                print("listeler yüklendi")
                time.sleep(0.5)
            except:
                print("liste kayıt dosyası bulunamadı...")
                time.sleep(3)
        elif commnd[0] == "payda":
            denominator = int(commnd[1])
            print("payda =", denominator)
            
    except:
        print("hata")        

""" 0 = çıkışta, kontrol dışı   """
""" 1 = düşüşte  """
""" 2 = çıkışa başladı """
""" 3 = satın alındı"""

while 1:
    bar = ShadyBar(' Piyasa taranıyor...', max=len(liste))
    for i in range(len(liste)):
        bought_qty = pos.count(3)
        satin_liste = []
        canli_havuz = []
        satin_liste_indexes = [l for l, x in enumerate(pos) if x == 3]
        for j in range(len(satin_liste_indexes)):
            satin_liste.append(liste[satin_liste_indexes[j]])
        canli_havuz_indexes = [m for m, x in enumerate(pos) if x == 2]
        for k in range(len(canli_havuz_indexes)):
            canli_havuz.append(liste[canli_havuz_indexes[k]])
        interface =', '.join(canli_havuz)
        interface2 = ', '.join(satin_liste)
        interface3 = bought_qty
        print(" " + liste[i])
        print(" Canlı havuz: ",interface,"\n","Satın alınanlar: ",interface2,"(", interface3 ,")","\n",)
        info1d = indicators1d(liste[i])
        limit_sat = (((math.pow((float(info1d["fastd"][-1])+float(info1d["fastk"][-1]))/2,2))/1200)+0.55)
        limit_al = (((math.pow((float(info1d["fastd"][-1])+float(info1d["fastk"][-1]))/2,2))/1600)+3)
        if pos[i] == 0 and info1d["fastd"][-1]>info1d["fastk"][-1]+limit_al:
            pos[i] = 1
        if pos[i] == 1 and info1d["fastk"][-1]>info1d["fastd"][-1]+limit_al:
            pos[i] = 2
        if pos[i] == 2:
            info1h = indicators1h(liste[i])
            info4h = indicators4h(liste[i])
            if bought_qty < denominator and info1d["fastk"][-1]>info1d["fastd"][-1]+limit_al and info1h["fastk"][-1]>info1h["fastd"][-1]+limit_al and info4h["fastk"][-1]>info4h["fastd"][-1]+limit_al and info1h["fastk"][-1]<50 and info4h["fastk"][-1]<50: 
                qty = buy(liste[i],bought_qty,denominator)
                if qty["origQty"] != 0:
                    pos[i] = 3
                bought_qty = pos.count(3)
            elif info1d["fastd"][-1]>info1d["fastk"][-1]:
                pos[i] = 1
            elif bought_qty >= denominator:
                pos[i] = 0
        if pos[i] == 3 and info1d["fastd"][-1]>info1d["fastk"][-1]+limit_sat:
            sellqty = sell(liste[i])
            pos[i] = 1
        if bought_qty == denominator:
            pass
        open_file = open("pos.dat", "wb")
        pickle.dump(pos, open_file)
        open_file.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        bar.next()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    