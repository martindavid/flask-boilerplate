import pytest


@pytest.fixture(scope="session")
def app():
    """Global skylines application fixture

    Initialized with testing config file.
    """
    yield create_app(config_file=config.TESTING_CONF_PATH)


@pytest.fixture(scope="function")
def files_folder(app):
    """
    Creates a clean upload folder
    """
    filesdir = app.config['SKYLINES_FILES_PATH']
    if os.path.exists(filesdir):
        shutil.rmtree(filesdir)

    os.makedirs(filesdir)


@pytest.fixture(scope="session")
def db(app):
    """Creates clean database schema and drops it on teardown

    Note, that this is a session scoped fixture, it will be executed only once
    and shared among all tests. Use `db_session` fixture to get clean database
    before each test.
    """
    assert isinstance(app, SkyLines)

    setup_db(app)
    yield database.db
    teardown_db()


@pytest.fixture(scope="function")
def db_session(db, app):
    """Provides clean database before each test. After each test,
    session.rollback() is issued.

    Return sqlalchemy session.
    """
    assert isinstance(app, SkyLines)

    with app.app_context():
        clean_db()
        yield db.session
        db.session.rollback()
