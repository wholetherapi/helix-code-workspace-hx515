from src.main import run


def test_run_returns_dict():
    assert isinstance(run(), dict)
