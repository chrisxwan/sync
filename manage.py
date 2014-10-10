import os
from app import myapp, db
from app.models import User
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell


manager = Manager(myapp)
migrate = Migrate(myapp, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	myapp.run(debug=True)
