from importlib import import_module

# Reuse the package migration without copying its schema into the test project.
Migration = import_module("baseapp_pages.migrations.0001_initial").Migration
