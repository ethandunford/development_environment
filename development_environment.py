#-- ----------------------------------------------------------------------------
#--
#-- Title:        development_environment.py
#-- Desc:         Download all necessary software for development 
#-- License:      Apache License https://www.apache.org/licenses/LICENSE-2.0
#-- Author:       Ethan Dunford
#-- Date:         18/01/2017
#-- Version:      0.1
#-- ----------------------------------------------------------------------------
import os

class Ubuntu(object):

    #-- system tools
    #-- ------------------------------------------------------------------------
 
    def update(self):
        os.system('sudo apt-get update')

    def remove_lock(self):
        os.system('sudo rm /var/cache/apt/archives/lock')
        os.system('sudo rm /var/lib/dpkg/lock')

    def autoremove(self):
        os.system('apt-get -y autoremove')


    def install_curl(self):
        os.system('sudo apt-get install curl')

    def install_git(self):
        os.system('sudo apt-get install git')


    #-- webservers
    #-- ------------------------------------------------------------------------

    def install_apache(self):
        os.system('sudo apt-get install apache2')
        os.system('sudo ufw app info "Apache Full"')

    def restart_apache(self):
        os.system('sudo systemctl restart apache2')

    def reload_apache(self):
        os.system('sudo systemctl reload apache2')

    def install_node(self):
        os.system('sudo apt-get install nodejs')
        os.system('sudo apt-get install npm')


    #-- lanagauges
    #-- ------------------------------------------------------------------------
 
    def install_python_three(self):
        os.system('sudo apt-get -y upgrade')
        os.system('sudo apt-get install -y python3-pip')
        os.system('sudo apt-get install build-essential libssl-dev libffi-dev python-dev')
        os.system('sudo apt-get install -y python3-venv')

    def install_pip_python_two(self):
        os.system('sudo apt-get install python-pip')

    def install_pip_python_three(self):
        os.system('sudo apt-get install python3-pip')


    def install_php_seven(self):
        os.system('sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql')

    def php_seven_show_errors(self):
        os.system('sudo sed -i "s/display_startup_errors = Off/display_startup_errors = On/g" /etc/php/7.0/apache2/php.ini')
        os.system('sudo sed -i "s/display_errors = Off/display_errors = On/g" /etc/php/7.0/apache2/php.ini')
        self.reload_apache()


    #-- database
    #-- ------------------------------------------------------------------------
 
    def install_postgres(self):
        os.system('sudo apt-get install postgresql postgresql-contrib')

    def allow_local_postgres(self):
        os.system('sudo sed -i "s/#listen_addresses = \'localhost\'/listen_addresses = \'*\'/g" /etc/postgresql/9.5/main/postgresql.conf')
        os.system('echo "host    all             all             0.0.0.0/0               md5" | sudo tee -a /etc/postgresql/9.5/main/pg_hba.conf')
        self.reload_postgres()

    def restart_postgres(self):
        os.system('sudo systemctl restart postgresql')

    def reload_postgres(self):
        os.system('sudo systemctl reload postgresql')

    def install_mysql(self):
        os.system('sudo apt-get install mysql-server')
        os.system('mysql_secure_installation')


    #-- containers
    #-- ------------------------------------------------------------------------

    def install_docker(self):
        self.install_curl()
        os.system('sudo apt-get install apt-transport-https ca-certificates curl software-properties-common')
        os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
        os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"')
        self.update()
        os.system('apt-cache search docker-ce')
        os.system('Install docker-ce')
        os.system('sudo apt-get install docker-ce')


    #-- software
    #-- ------------------------------------------------------------------------

    def install_sublime(self):
        self.install_curl()
        os.system('curl -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
        os.system('sudo apt-get install apt-transport-https')
        os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
        self.update()
        os.system('sudo apt-get install sublime-text')

    def install_atom(self):
        os.system('sudo add-apt-repository ppa:webupd8team/atom')
        self.update()
        os.system('sudo apt install atom')

    def install_dbeaver(self):
        os.system('wget https://dbeaver.jkiss.org/files/dbeaver-ce_latest_amd64.deb')
        os.system('sudo dpkg -i dbeaver-ce_latest_amd64.deb')
        os.system('rm dbeaver-ce_latest_amd64.deb')
        os.system('sudo apt-get -f install')

    def install_filezilla(self):
        self.update()
        os.system('sudo apt-get install filezilla')

    def install_chrome(self):
        os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
        os.system('echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list')
        self.update()
        os.system('sudo apt-get install google-chrome-stable')

    def install_skype(self):
        os.system('wget https://repo.skype.com/latest/skypeforlinux-64.deb')
        os.system('sudo dpkg -i skypeforlinux-64.deb')
        os.system('sudo apt install -f')
        os.system('sudo rm -rf skypeforlinux-64.deb')

    #-- Development stacks
    #-- ------------------------------------------------------------------------

    def lamp_stack(self, show_errors=False):
        self.update()
        self.install_apache()
        self.install_php_seven()        
        if show_errors is True:        
            self.php_seven_show_errors()
        self.install_mysql()

    def lapp_stack(self):
        self.update()
        self.install_apache()
        self.install_php_seven()        
        if show_errors is True:        
            self.php_seven_show_errors()
        self.install_postgres()

    def setup(self):
        self.update()
        self.install_curl()
        self.install_git()
        self.install_sublime()
        self.install_atom()
        self.install_dbeaver()
        self.install_filezilla()
        self.install_docker()
        self.install_chrome()
        self.install_skype()
        self.install_node()
        self.install_apache()
        self.install_python_three()
        self.install_php_seven()
        self.php_seven_show_errors()
        self.install_postgres()
        self.allow_local_postgres()



#-- Example 
#-- ----------------------------------------------------------------------------

# u = Ubuntu()
# u.setup()
