from functools import wraps
from django.conf import settings
from django import http
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import six
from django.utils.module_loading import import_string
from importlib import import_module

json = import_module(getattr(settings, 'JSON_MODULE', 'json'))
JSON = getattr(settings, 'JSON_DEFAULT_CONTENT_TYPE', 'application/json')


def _dump_json(data):
    options = {}
    options.update(getattr(settings, 'JSON_OPTIONS', {}))

    # Use the DjangoJSONEncoder by default, unless cls is set to None.
    options.setdefault('cls', DjangoJSONEncoder)
    if isinstance(options['cls'], six.string_types):
        options['cls'] = import_string(options['cls'])
    elif options['cls'] is None:
        options.pop('cls')

    return json.dumps(data, **options)


def json_auth(*args, **kwargs):
    content_type = kwargs.get('content_type', JSON)

    def decorator(f):
        @wraps(f)
        def wrapped(request, *a, **kw):
            if request.user.is_authenticated():
                return f(request, *a, **kw)
            else:
                message = _dump_json({'message': 'not authenticated'})
                return http.HttpResponse(
                    message, status=405, content_type=JSON)
        return wrapped
    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    else:
        return decorator
