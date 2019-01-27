from boto3 import client
import sys
import boto3

s3 = boto3.resource('s3')

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3


mybucket = s3.Bucket('www.medhost.com')



print 'stopping...'
sys.exit()



for object in mybucket.objects.filter(Prefix='eLearning/interactive'):
	oldfile = object.key
	newfile = oldfile.lower()

	if (oldfile != newfile):
		# print (oldfile)
		print (newfile)

		s3.Object('www.medhost.com',newfile).copy_from(CopySource={'Bucket': 'www.medhost.com', 'Key': oldfile})
		#s3.Object('www.medhost.com',oldfile).delete()



for object in mybucket.objects.filter(Prefix='eLearning/video'):
	oldfile = object.key
	newfile = oldfile.lower()

	if (oldfile != newfile):
		# print (oldfile)
		print (newfile)

		s3.Object('www.medhost.com',newfile).copy_from(CopySource={'Bucket': 'www.medhost.com', 'Key': oldfile})
		#s3.Object('www.medhost.com',oldfile).delete()


sys.exit()





# for object in mybucket.objects.all():
# 	 oldfile = key['Key'];
#     #print (k)
#     newfile = oldfile.lower();

#      if (oldfile != newfile):
#        # print (oldfile)
#         print (newfile)

#         #s3.Object('www.medhost.com',newfile).copy_from(CopySource={'Bucket': 'www.medhost.com', 'Key': oldfile})
#         #s3.Object('www.medhost.com',oldfile).delete()
#     else:
#     	print ('*************' + oldfile)


# 	if (str(object).find('temp')):
#     print(str(object).find('temp'))

# sys.exit()

for key in conn.list_objects(Bucket='www.medhost.com', MaxKeys=999999999)['Contents']:
    oldfile = key['Key'];
    #print (k)
    newfile = oldfile.lower();

   # if (oldfile.find('interactive')):
   # 	print (oldfile)
   # 	sys.exit()

    if (oldfile != newfile):
       # print (oldfile)
        print (newfile)

        #s3.Object('www.medhost.com',newfile).copy_from(CopySource={'Bucket': 'www.medhost.com', 'Key': oldfile})
        #s3.Object('www.medhost.com',oldfile).delete()
    else:
    	print ('*************' + oldfile)
        