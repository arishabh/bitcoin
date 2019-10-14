#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : past_data.py
# Author            : Rishabh Agrawal <rishabhagrawal41@gmail.com>
# Date              : 14.10.2019
# Last Modified Date: 14.10.2019
from requests import get
from bs4 import BeautifulSoup as bs
from datetime import datetime

today = datetime.now()

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end="+str(today.year)+str(today.month)+str(today.day)

cont = bs(get(url).content, "lxml")

date = []
rate = []
for entry in cont.findAll("tr", {"class":"text-right"}):
    info = entry.get_text().split("\n")
    date.append(datetime.strptime(info[1], "%b %d, %Y"))
    rate.append(info[2])

with open("data.txt", "w+") as f:
    for i in range(len(rate)):
        f.write(str(date[i]) + "\t" + str(rate[i]) + "\n")
