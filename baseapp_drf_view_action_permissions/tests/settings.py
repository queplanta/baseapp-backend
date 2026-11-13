from baseapp_core.tests.settings import *  # noqa

INSTALLED_APPS += [
    "baseapp_drf_view_action_permissions",
    "baseapp_drf_view_action_permissions.tests",
]
AUTH_USER_MODEL = "baseapp_drf_view_action_permissions_tests.DRFUser"
ROOT_URLCONF = "baseapp_drf_view_action_permissions.tests.urls"
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = (
    "rest_framework.authentication.SessionAuthentication",
)

MIDDLEWARE += [
    "baseapp_drf_view_action_permissions.middleware.RestrictIpMiddleware",
]
