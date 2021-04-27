import os
import pytest


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, 'picture.png')