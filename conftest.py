from pathlib import Path


def pytest_ignore_collect(collection_path, config):
    """Run the permissions package only in its dedicated settings invocation."""
    package_tests = Path(config.rootpath, "baseapp_drf_view_action_permissions")
    if Path(collection_path) != package_tests:
        return None

    explicitly_requested = any(
        Path(argument).resolve() == package_tests.resolve() for argument in config.args
    )
    return not explicitly_requested
