# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import *
data=[(0,0,'start',0.712),(0,0,'end',1.520),(0,1,'start',3.140),(0,1,'end',4.120),
      (1,0,'start',0.550),(1,0,'end',1.550),(1,1,'start',0.430),(1,1,'end',1.420),
      (2,0,'start',4.100),(2,0,'end',4.512),(2,1,'start',2.500),(2,1,'end',5.000)]
schema=["Machine_id","processid","activityid","timestamp"]
df1=spark.createDataFrame(data,schema)
display(df1)

# COMMAND ----------

df2=df1.select("Machine_id","processid" ,when(df1.activityid=='start', df1.timestamp).alias('starttime'),when(df1.activityid=='end', df1.timestamp).alias('endtime'))
df3=df2.groupBy(df2.Machine_id,df2.processid).agg(max(df2.starttime).alias('starttime'),max(df2.endtime).alias('endtime'))
df4=df3.select(df3.Machine_id,(df3.endtime-df3.starttime).alias('timediff'))
display(df4.groupBy("Machine_id").agg(avg(df4.timediff)).alias('average_time'))

# COMMAND ----------


