from unittest.mock import patch

from cli import App


def test_run_method_exists():
    app = App()
    assert hasattr(app, "run")
    assert callable(app.run)


def test_start_method(capsys):
    app = App()
    text = "hello world hello"
    top_n = 2

    app.start(text, top_n)

    captured = capsys.readouterr()
    assert "hello" in captured.out
    assert "world" in captured.out


@patch("builtins.input", return_value="test text input")
@patch("cli.parse_args")
def test_run_with_input(mock_parse_args, mock_input, capsys):
    from argparse import Namespace

    mock_parse_args.return_value = Namespace(file=None, top=2)
    app = App()
    app.run()

    captured = capsys.readouterr()
    assert "test" in captured.out
