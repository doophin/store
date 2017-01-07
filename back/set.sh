#!/bin/bash
if [ $1 = cffexi ] && [ $2 ];then
sed -i 's/'`cat /dailydata/cffexinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/cffexinterest/src/dbcfg.properties
elif [ $1 = dcei ] && [ $2 ];then
sed -i 's/'`cat /dailydata/dceinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/dceinterest/src/dbcfg.properties
elif [ $1 = shfei ] && [ $2 ];then
sed -i 's/'`cat /dailydata/shfeinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/shfeinterest/src/dbcfg.properties
elif [ $1 = czcei ] && [ $2 ];then
sed -i 's/'`cat /dailydata/czceinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/czceinterest/src/dbcfg.properties
elif [ $1 = cffexq ] && [ $2 ];then
sed -i 's/'`cat /dailydata/cffexquote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/cffexquote/src/dbcfg.properties
elif [ $1 = dceq ] && [ $2 ];then
sed -i 's/'`cat /dailydata/dcequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/dcequote/src/dbcfg.properties
elif [ $1 = shfeq ] && [ $2 ];then
sed -i 's/'`cat /dailydata/shfequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/shfequote/src/dbcfg.properties
elif [ $1 = czceq ] && [ $2 ];then
sed -i 's/'`cat /dailydata/czcequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$2'/g' /dailydata/czcequote/src/dbcfg.properties
elif [ $1 -gt 0 ] && [ ! $2 ];then
sed -i 's/'`cat /dailydata/cffexinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/cffexinterest/src/dbcfg.properties
sed -i 's/'`cat /dailydata/dceinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/dceinterest/src/dbcfg.properties
sed -i 's/'`cat /dailydata/shfeinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/shfeinterest/src/dbcfg.properties
sed -i 's/'`cat /dailydata/czceinterest/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/czceinterest/src/dbcfg.properties
sed -i 's/'`cat /dailydata/cffexquote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/cffexquote/src/dbcfg.properties
sed -i 's/'`cat /dailydata/dcequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/dcequote/src/dbcfg.properties
sed -i 's/'`cat /dailydata/shfequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/shfequote/src/dbcfg.properties
sed -i 's/'`cat /dailydata/czcequote/src/dbcfg.properties| grep date= | cut -d= -f2`'/'$1'/g' /dailydata/czcequote/src/dbcfg.properties
else
echo "请直接输入日期更改所有。
或者指定交易所加i(持仓)或q(行情)并加上日期。
如 dateset dcei 20170101"
fi
