import importlib
import logging
from types import ModuleType

from django.conf import settings
from django.contrib.auth import get_user_model

logger = logging.getLogger('ansible_base.authentication.views.authenticator_users')


def get_authenticator_user_view():
    try:
        user_viewset_name = settings.ANSIBLE_BASE_USER_VIEWSET
        module_name, _junk, class_name = user_viewset_name.rpartition('.')
        module = importlib.import_module(module_name, package=class_name)
        user_viewset_view = getattr(module, class_name)
        if isinstance(user_viewset_view, ModuleType):
            raise ModuleNotFoundError()

        class AuthenticatorPluginRelatedUsersView(user_viewset_view):
            def get_queryset(self, **kwargs):
                authenticator_id = kwargs.get('authenticator_id', None)
                if authenticator_id is None:
                    return get_user_model().objects.none()
                authenticator_users = get_user_model().objects.filter(authenticator_user__provider__id=authenticator_id)
                return authenticator_users

        return AuthenticatorPluginRelatedUsersView
    except ModuleNotFoundError:
        logger.error("ANSIBLE_BASE_USER_VIEWSET was not an APIView")
    except AttributeError:
        logger.debug("ANSIBLE_BASE_USER_VIEWSET was not specified")

    return None