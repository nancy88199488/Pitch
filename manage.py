from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import  Manager, Server
from app.models import User,Pitch,Comment,Upvote,Downvote
from  flask_migrate import Migrate

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch=Pitch,Comment=Comment,Upvote=Upvote,Downvote=Downvote)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()