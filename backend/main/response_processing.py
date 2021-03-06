from rest_framework.response import Response


def reject_response():
    return get_error_response(400)


def unauthorized_response():
    return get_error_response(401)


def server_error_response():
    return get_error_response(500)


def cors_response():
    return setup_cors_response_headers(Response(status=204))


""""""""""""""""""""""""""""""""""""""""""""""""
"    Warning:                                  "
"    The functions below are the inner         "
"    functions and shouldn't be used outside   "
""""""""""""""""""""""""""""""""""""""""""""""""


def setup_cors_response_headers(res):
    # TODO: put origin inside the config.
    res["Access-Control-Allow-Origin"] = "http://localhost:1329, http://127.0.0.1:1329"
    # TODO: create allow_method decorator.
    res["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    res["Access-Control-Allow-Headers"] = \
        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    res["Access-Control-Allow-Credentials"] = "true"
    return res


def get_success_response(body={}):
    return setup_cors_response_headers(Response(body, status=200, content_type="application/json"))


def get_error_response(status_code):
    return setup_cors_response_headers(Response(status=status_code, content_type="application/json"))
