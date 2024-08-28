mkdir -p /media/ENM
sudo mount -o loop /software/ENM/$1  /media/ENM
yum install -y /media/ENM/repos/ENM/ms/ERICenminst_CXP9030877*
sudo umount /media/ENM
rmdir /media/ENM  
