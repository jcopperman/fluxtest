def pytest_configure(config):
    config.addinivalue_line("markers", "test: mark a test as a test.")
