from app create_app,db

app = create_app('production')

manager = manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add.command('serve',Server)
if __name__ == '__main__':
    manager.run()