from fabric.api import *

#ssh -i /Users/rl011787/.ec2/whoopee.pem ubuntu@ec2-54-245-154-154.us-west-2.compute.amazonaws.com
env.hosts = ['ec2-54-245-154-154.us-west-2.compute.amazonaws.com']
env.user = 'ubuntu'
env.key_filename = '/Users/rl011787/.ec2/whoopee.pem'

def apt_install():
    run('sudo apt-get update')
    run('sudo apt-get install python-dev')
    run('sudo apt-get install gcc-4.7')
    run('sudo apt-get install python-pip')
    run('sudo apt-get install nginx')
    run('sudo apt-get install python-dev postgresql-server-dev-all')
    run('sudo apt-get install postgresql python-psycopg2')
    run('sudo apt-get install git')


def pip_install():
    run('sudo pip install virtualenv')
    run('sudo pip install virtualenvwrapper')
    run('sudo pip install Django')
    run('sudo pip install argparse')
    run('sudo pip install django-classy-tags')
    run('sudo pip install django-i18nurls')
    run('sudo pip install django-mptt==0.5.5')
    run('sudo pip install django-sekizai')
    run('sudo pip install gunicorn')
    run('sudo pip install html5lib')
    run('sudo pip install psycopg2')
    run('sudo pip install wsgiref')

def create_virtualenv():
    run('echo export WORKON_HOME=$HOME/.virtualenvs >> $HOME/.bashrc')
    run('echo export PROJECT_HOME=$HOME/Devel >> $HOME/.bashrc')
    run('echo source /usr/local/bin/virtualenvwrapper.sh >> $HOME/.bashrc')

    with cd('/home/ubuntu'):
        run('source .bashrc')
        
def git_code():
    with cd('/home/ubuntu/'):
        run('git clone https://github.com/roger-link/whoopdeedoo.tv.git')
        run('mv whoopdeedoo.tv/ wdd/')

def setup_nginx():
        run('sudo mkdir -p /opt/django/logs/nginx/')
        run('sudo ln -s $HOME/wdd/static /opt/django')
        run('sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup')
        run('wget https://bitbucket.org/deccico/django_gunicorn/raw/tip/server/etc/nginx/sites-available/default')
        run('sudo cp default /etc/nginx/sites-available/default')

def restart_nginx():
    run('sudo service nginx restart')

def start_gunicorn():
    with cd('/home/ubuntu/wdd'):
        run('gunicorn_django -b 0.0.0.0:8000')

def install_postgres():
    # Create PostgreSQL user and enter password
    run('sudo -u postgres createuser -SDRP bla')
    # Create PostgreSQL database
    run('sudo -u postgres createdb -E utf8 -O bla bla')
    run('sudo echo host    all             all              0.0.0.0/0              md5 >> /etc/postgresql/9.1/main/pg_hba.conf')

def deploy():
    apt_install()
    pip_install()
    create_virtualenv()
    setup_nginx()
    restart_nginx()
    git_code()
    start_gunicorn()
