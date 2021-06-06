import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
import csv
import codecs
import os
import itertools
from datetime import datetime
'''
print(df.columns.values)
['hotel' 'is_canceled' 'lead_time' 'arrival_date_year' 'arrival_date_month' 'arrival_date_week_number'
 'arrival_date_day_of_month' 'stays_in_weekend_nights' 'stays_in_week_nights' 'adults' 'children' 'babies' 'meal' 
 'country' 'market_segment' 'distribution_channel' 'is_repeated_guest' 'previous_cancellations'
 'previous_bookings_not_canceled' 'reserved_room_type' 'assigned_room_type' 'booking_changes' 'deposit_type' 
 'agent' 'company' 'days_in_waiting_list' 'customer_type' 'adr' 'required_car_parking_spaces' 
 'total_of_special_requests' 'reservation_status' 'reservation_status_date']
'''
os.getcwd() #获取当前工作路径
df = pd.read_csv('D:/1007storage/visual_studio/Python/data/hotel_bookings.csv') #读取数据
#print(df.info())

#df1 = df.fillna(count_price)#winepirce2   用众数填充nan
ssss1 = [91647,14284,10612,1152,773]
def num_nan(nums):
    print("the number of nan________")
    x2 = nums.isnull().sum().sum()    #读取nums中的nan值
    return x2 
hang1 = range(0,119390)
hang2 = [4,6,9,11]
def pre(nums):
    for temppre in hang1:
        if nums['arrival_date_day_of_month'][temppre] > 31:
            nums['arrival_date_day_of_month'][temppre] = 31
    print("finish")          
#pre(df)




#print(num_nan(df.is_canceled))
#print(df.info())
print("________")
#print(df['meal'].unique()) 
#print(num_nan(df['meal']))
def jiben(len11111):
    print("##################对基本情况进行处理##################")
    hotel = ["Resort Hotel","City Hotel"]
    is_canceled = [0,1]
    #基本情况：城市酒店和假日酒店预订需求和入住率比较
    df1 = df[['hotel','is_canceled']]
    vc11 = df['hotel'].value_counts()
    print("Resort Hotel和 City Hotel的预定需求统计")
    #print(vc11)
    #入住率分析
    group1 = df1.groupby(df['hotel'])
    i = 1
    for temp in hotel:
        print("---------------------------------")
        print(temp,"预定数 = ", vc11[i])
        i = i - 1
        #print(group1.get_group(temp))
        group12 = pd.DataFrame(group1.get_group(temp))
        vc12 = group1.get_group(temp).value_counts()#对每种旅馆的取消预定与否进行计数
        #print(vc12)
        sum_lead = vc12[0] + vc12[1]
        print(temp,"预定率 = ", (vc12[1]/sum_lead))
        print("---------------------------------")
        print(temp,"退订率 = ", (vc12[0]/sum_lead))
        print("---------------------------------")

#print("##################对客户行为进行处理##################")
#print("879879879879879879879",num_nan(df.meal))
#对提前预定时间lead_time、入住时长、预订间隔、餐食预订情况进行处理
#print("---提前预定时间lead_time---")
def leadtime(dddddd):
    print("提前预定时间的统计")
    vc21 = df['lead_time'].value_counts()#对提前预定时间的统计
    print(vc21)
    filepath = "D:/1007storage/visual_studio/Python/datamingwork2/data/csv/lead_time.csv"
    vc21.to_csv(filepath,sep=',')   #将对提前预定时间的统计写入lead_time_counts.csv中
    #一年中最佳预订酒店时间
    ltc = pd.read_csv("D:/1007storage/visual_studio/Python/datamingwork2/data/csv/lead_time_counts.csv")
    #print(ltc['lead_time'])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #print(df['babies'].unique())




def meal(dddfff):
    #用餐情况
    print(df['meal'].value_counts())
    babies = [0,1,2,9,10]
    meal = ['BB','FB','HB','SC','Undefined']
    df22 = df[['babies','meal']]
    group22 = df22.groupby(df['babies'])
    vc22 = df22['babies'].value_counts()
    print(vc22)
    i2112 = 0
    for temp in babies:
        if temp == 0:
            newlie = [0,0,0,0,0]
        if temp == 1:
            newlie = [0,0,0,0,0]
        if temp == 2:
            newlie = [0,0]
        if temp == 9:
            newlie = [0]
        if temp == 10:
            newlie = [0]
        print("---------------------------------")
        print("婴儿数量 = ",temp)
        group21 = pd.DataFrame(group22.get_group(temp))
        #print(group21)
    
        vc221 = group22.get_group(temp) #获取当babies为temp时的meal数据
        #print(vc221)
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        vc2213 = vc221.value_counts()   #统计babies为temp时的meal数量
        #print(vc2213[i2112][0])
        #print("meal种类数",vc2213[temp].shape[0])
        #print("newlie初始化",newlie)
        len = vc2213[temp].shape[0]
        #print("len = ",len)
        ssss = range(0,len) #len为babies为temp时的meal种类
        for temp1 in ssss:
            newlie[temp1] = vc2213[temp][temp1] / vc22[temp]
        #print(newlie)
        vc22131 = pd.DataFrame(vc2213)  #将vc2213转化为dataframe格式
        #newlie1 = pd.DataFrame(newlie)
        print(":::::::::::::::::::::::::::::::::::")
        #print(vc2213)
        #for temp2 in ssss:
        #vc2213['percent'] = newlie
        vc22131.insert(1,'percent',newlie)
        i2112 = i2112 + 1
        print("meal的统计:")
        print(vc22131)
#kkk123 = 0
#meal(kkk123)

#一年中最佳的预定酒店的时间'arrival_date_week_number' ''

def timetrans():
    df3 = df[['lead_time','arrival_date_year','arrival_date_month','arrival_date_day_of_month']]
    #print(df3.info())
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    #df3['data']=df3.id.apply().
    #df3['data'] = df3['lead_time'] - df3['lead_time']
    hang = range(0,119390)
    df3['data'] = np.nan
    df3['lead_times'] = np.nan
    print(df3['lead_times'])
    for temp31 in hang:
        print(df3['arrival_date_year'][temp31],df3['arrival_date_month'][temp31],df3['arrival_date_day_of_month'][temp31])
        df3['data'][temp31] = datetime(df3['arrival_date_year'][temp31], df3['arrival_date_month'][temp31], df3['arrival_date_day_of_month'][temp31])
        df3['lead_times'][temp31] = df3['data'][temp31] + pd.Timedelta(days=0-df3['lead_time'][temp31])
    filepath = "D:/1007storage/visual_studio/Python/data/df3.csv"
    df3.to_csv(filepath,sep=',')
    print(df3)
    return 'trans finish'



print("-----一年中最佳的预定酒店的时间----")
def tans_m_d():
    
    df31 = pd.read_csv("D:/1007storage/visual_studio/Python/data/df3.csv")  #读取转换为时间格式的数据
    #print(df31.info())
    df31['lock_time'] = pd.to_datetime(df31['lead_times'])

    df31['lock'] = pd.to_datetime(df31['data'])
    #print(df31.info())
    for temp30 in hang1:
        df31['lock'][temp30] = df31['lock_time'][temp30].strftime("%m-%d")
        #print("1")
    print(df31)
    filepath = "D:/1007storage/visual_studio/Python/datamingwork2/data/csv/lead_times.csv"
    df31.to_csv(filepath,sep=',')   #将月-日数据录入lead_times.csv中列号为lock
    print("finish")

#hang30 = range(0,119390)
df312 = pd.read_csv("D:/1007storage/visual_studio/Python/data/lead_times.csv")
#df3121 = df312['lock']
vc31 = df312['lock'].value_counts() #value_counts()返回值为series
len31 = vc31.shape[0]
hang31 = range(0,len31)
vc311 = pd.DataFrame(vc31)
sum311 = 0
for temp311 in hang31:
    sum311  = sum311 + vc311['lock'][temp311]
print(sum311)
print("-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")
vc311['percents'] = '0'
for temp31 in hang31:
    vc311['percents'][temp31] = vc311['lock'][temp31] / 119390
    vc311['percents'][temp31] = vc311['percents'][temp31] * 1000000
    vc311['percents'][temp31] = int(vc311['percents'][temp31] / 100)
    vc311['percents'][temp31] = vc311['percents'][temp31] / 100
    vc311['percents'][temp31] = str(vc311['percents'][temp31]) + "%"
filepath = "lead_time_fenbu.csv"
vc311.to_csv(filepath,sep=',')
print(vc311)
#print(df312.info())



'''
df311 = pd.DataFrame(df31['lock'].value_counts())
df311['leads'] = np.nan
print(df311)
len311 = df311.shape[0]
hang31 = range(0,len311)

print(df311)

df312 = pd.DataFrame(df31['lead_times'].value_counts())
df312['percent'] = '0'
print(df312)
len31 = df31['lead_times'].value_counts().shape[0]
hang31 = range(0,len31)
print(df312)
print(df312.info())

for temp311 in hang31:
    df311['percent'][temp311] = df311[0][temp311].strftime("%m-%d")
print(df311.head(100))
'''








#利用Logistic预测酒店预订