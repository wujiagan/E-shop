# coding: utf-8

from jing.modules.passport.models import User, Role
from werkzeug import check_password_hash, generate_password_hash
from jing.core.database import dbs

class Populate(object):
    def __init__(self, db, *args, **kwargs):
        self.db = db
        self.args = args
        self.kwargs = kwargs
        self.roles = {}
        self.users = {}
        self.channels = {}

    def __call__(self, *args, **kwargs):
        self.create_users()

    def role(self, name):
        if not name in self.roles:
            role = Role.query.filter_by(name=name).first()
            if not role:
                role = Role.create(name)
            self.roles[name] = role
            
            if role:
                print("Created role: {0}".format(name))
        return self.roles.get(name)

    def create_users(self):
        self.users_data = [
            {
                "name": "admin@fn315.com",
                "email": "admin@fn315.com",
                "password": "123456",
                "roles": [self.role('admin')]
            },
            {
                "name": "viewer@fn315.com",
                "email": "viewer@fn315.com",
                "password": "123456",
                "roles": [self.role('viewer')]
            },
            {
                "name": "editor@fn315.com",
                "email": "editor@fn315.com",
                "password": "123456",
                "roles": [self.role('editor')]
            },
            {
                "name": "member@fn315.com",
                "email": "member@fn315.com",
                "password": "123456",
                "roles": [self.role('member')]
            },
        ]

        for data in self.users_data:
            name = data.get('name')
            pwd = data.get("password")
            if not name in self.users:
                user = User()
                user.username = data.get("name")
                user.email = data.get("email")
                user.password = generate_password_hash(data.get("password"))
                user.roles = data.get("roles")
                dbs.session.add(user)
                dbs.session.commit()
                self.users[name] = user
                print("User: mail:{o.email} pwd:{pwd}".format(o=user, pwd=pwd))

