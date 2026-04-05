
"""Tests for the example_pkg module."""


def test_example(capsys):
    """Test that example_pkg.main() prints the expected greeting message."""
    import example_pkg

    example_pkg.main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from example-pkg!\n"
