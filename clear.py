import os
import datetime
workpath='/root/CSU_China_Union_autoLogin/'
deleteDir=workpath+str(datetime.date.today()-datetime.timedelta(days=3))
# print(deleteDir)
if os.path.exists(deleteDir):
    os.removedirs(deleteDir)