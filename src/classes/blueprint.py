from flask import Blueprint

method_names = ['get', 'post', 'put', 'delete']


def register_method(blueprint, c, path, method, **options):
    endpoint = options.pop('endpoint', getattr(c, method).__name__)
    blueprint.add_url_rule(rule=path, endpoint=endpoint, view_func=getattr(c, method)(1), **options)


def bp(blueprint, class_name, path, methods=[], **options):
    def decorator(c):
        if len(methods) > 0:
            # Add default methods
            for method in methods:
                if method in method_names:
                    _method = '_method_' + class_name + '_' + method

                    # _method: this method name should be dynamic
                    @blueprint.route(rule=path, methods=[method])
                    def _method(**params):
                        return getattr(class_name, method)(**params)
        else:
            overwritten_methods = [a for a in dir(c) if not a.startswith('_')]
            # If we want to overwrite some methods
            if len(overwritten_methods) > 0:
                for method in overwritten_methods:
                    # Check if the method is allowed
                    if method in method_names:
                        register_method(blueprint=blueprint, c=c, path=path, method=method, **options)
    return decorator
