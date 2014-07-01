sudo ~/pve/bin/pybabel extract -F babel.cfg -o messages.pot .
sudo ~/pve/bin/pybabel init -i messages.pot -d translations -l zh_CN