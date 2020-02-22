def response_by_success(success, is_remove=False):
    if success:
        code = 200 if not is_remove else 204
        return {'message': 'Operation completed successfully.'}, code
    return {'message': 'Unsuccessful operation.'}, 500
