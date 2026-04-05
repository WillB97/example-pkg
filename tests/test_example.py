import pytest


def test_example(capsys):
    import example_pkg

    example_pkg.main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from example-pkg!\n"
