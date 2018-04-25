import pytest
import logging
import chromalog

@pytest.fixture(scope="session")
def session_logger():
    chromalog.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug("created session scope logger")
    return logger


@pytest.fixture(scope="function", name="log")
def function_logger(request, session_logger):
    logger = session_logger.getChild(request.node.name)
    logger.debug("created function scope logger")
    return logger