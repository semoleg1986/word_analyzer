from cli import App


def test_run_method_exists():
    app = App()
    assert hasattr(app, "run")
    assert callable(app.run)
