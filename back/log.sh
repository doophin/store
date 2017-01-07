#!/bin/bash
echo "1、大商所持仓
2、郑商所持仓
3、上期所持仓
4、中金所持仓
5、大商所行情
6、郑商所行情
7、上期所行情
8、中金所行情
请输入对应编号查询日志文件：";read num
if [ $num == 1 ];then
cat /dailydata/dceinterest/date.log
elif [ $num == 2 ];then
cat /dailydata/czceinterest/date.log
elif [ $num == 3 ];then
cat /dailydata/shfeinterest/date.log
elif [ $num == 4 ];then
cat /dailydata/cffexinterest/date.log
elif [ $num == 5 ];then
cat /dailydata/dcequote/date.log
elif [ $num == 6 ];then
cat /dailydata/czcequote/date.log
elif [ $num == 7 ];then
cat /dailydata/dcequote/date.log
elif [ $num == 8 ];then
cat /dailydata/dcequote/date.log
fi
