def pytest_configure(config):
    """
    configure pytest
    """
    # add `ragas_ci`
    config.addinivalue_line(
        "markers", "ragas_ci: Set of tests that will be run as part of Ragas CI"
    )
