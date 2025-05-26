import os

import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.test.yml")


@pytest.fixture(scope="session")
def docker_compose_project_name():
    return "news_test"


@pytest.fixture(scope="session")
def docker_services(docker_compose, docker_compose_project_name):
    """Ensure all services are up and running."""
    docker_compose.up()
    yield
    docker_compose.down()
