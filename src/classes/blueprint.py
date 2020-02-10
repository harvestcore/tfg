from flask import Blueprint

method_names = ['get', 'post', 'put', 'delete']


def register_method(blueprint, bp_class, path, method, **options):
    endpoint = options.pop('endpoint', getattr(bp_class, method).__name__)
    blueprint.add_url_rule(rule=path, endpoint=endpoint, view_func=getattr(bp_class, method), methods=[method],
                           **options)


def bp(blueprint, bp_class, path, methods=[], **options):
    def decorator(c):
        if len(methods) > 0:
            # Add default methods
            for method in methods:
                if method in method_names:
                    item_method = ''
                    if method is 'get':
                        @blueprint.route()
                        def xd():
                            pass
                    if method is 'post':
                        @blueprint.route()
                        def xd():
                            pass
                    if method is 'put':
                        @blueprint.route()
                        def xd():
                            pass
                    if method is 'delete':
                        @blueprint.route()
                        def xd():
                            pass

                    register_method(blueprint=blueprint, bp_class=bp_class, path=path, method=method, **options)
        else:
            overwritten_methods = [a for a in dir(c) if not a.startswith('_')]
            # If we want to overwrite some methods
            if len(overwritten_methods) > 0:
                for method in overwritten_methods:
                    # Check if the method is allowed
                    if method in method_names:
                        register_method(blueprint=blueprint, bp_class=c, path=path, method=method, **options)
    return decorator
