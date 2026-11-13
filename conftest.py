from pathlib import Path


def pytest_ignore_collect(collection_path, config):
    """Collect the consolidated packages, not their legacy source copies."""
    root = Path(config.rootpath)
    path = Path(collection_path)
    package_tests = root / "baseapp_drf_view_action_permissions"
    if path == package_tests:
        explicitly_requested = any(
            Path(argument).resolve() == package_tests.resolve() for argument in config.args
        )
        return not explicitly_requested

    if path.parent == root and path.name.startswith("baseapp-"):
        return True

    return None
