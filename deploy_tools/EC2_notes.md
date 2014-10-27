chmod 400 qbank.pem

ssh -i ~/dropbox/webdev/tdd/qbank.pem ubuntu@54.69.108.137

../virtualenv/bin/python3 manage.py runserver

scp -i qbank.pem database/db.sqlite3 ubuntu@54.69.108.137:~/sites/54.69.108.137/database

scp -i ~/dropbox/webdev/tdd/qbank.pem -r database/ ubuntu@54.69.108.137:~/sites/54.69.108.137/

../virtualenv/bin/gunicorn qbank.wsgi:application

#kill port 8000
sudo fuser -k 8000/tcp

#ngix server restart
sudo service nginx reload

export SITENAME=54.69.108.137

cd ~/sites/54.69.108.137/source

export TAG=`date +DEPLOYED-%F/%H%M`

===================
Deployment:
===================

LOCAL: (in fab_deploy)
fab deploy -i ~/dropbox/webdev/tdd/qbank.pem -H ubuntu@54.69.108.137

SERVER: (in source)
#Create nginx virtual host

sed "s/SITENAME/54.69.108.137/g" \
deploy_tools/nginx.template.conf | sudo tee \
/etc/nginx/sites-available/54.69.108.137

#Activate & link file
sudo ln -s ../sites-available/54.69.108.137 \
/etc/nginx/sites-enabled/54.69.108.137

#Upstart script
sed "s/SITENAME/54.69.108.137/g" \
deploy_tools/gunicorn-upstart.template.conf | sudo tee \
/etc/init/gunicorn-qbank.conf

#Reload server and run upstart script
sudo service nginx reload
sudo stop gunicorn-qbank
sudo start gunicorn-qbank

===================
Update Deployment:
===================
LOCAL: (in fab_deploy)
fab deploy -i ~/dropbox/webdev/tdd/qbank.pem -H ubuntu@54.69.108.137

SERVER:
sudo restart gunicorn-qbank

FT
python3 manage.py test functional_tests --liveserver=nsqbank.com