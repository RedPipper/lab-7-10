from console import consola
import pytest

pytest.main(args=["tests/domain_tests.py","tests/repo_tests.py","tests/service_tests.py"])

app = consola()
app.start()

