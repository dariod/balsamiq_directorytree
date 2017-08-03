import os
 
print 'F ' + os.path.basename(os.getcwd())
dirlist=os.listdir(os.getcwd())
while len(dirlist) > 0:
    dirname=dirlist.pop(0)
    if os.path.isdir(dirname):
        print len(dirname.split('/')) * ' ' + ' '.join(['F',os.path.basename(dirname)])
        for item in os.listdir(dirname):
            dirlist.insert(0,os.path.join(dirname,item))
    if os.path.isfile(dirname):
        print len(dirname.split('/')) * ' ' + ' '.join(['-',os.path.basename(dirname)])
