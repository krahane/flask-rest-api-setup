template = {
    "swagger": "2.0",
    "info": {
        "title": "Employee Data",
        "description": "API for Employees",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "deve@gmail.com",
            "url": "www.twitter.com/deve",
        },
        "termsOfService": "www.twitter.com/deve",
        "version": "1.0"
    },
    "basePath": "/api",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        # "Bearer": {
        #     "type": "apiKey",
        #     "name": "Authorization",
        #     "in": "header",
        #     "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        # }
        'oauth2': {
        'type': 'oauth2',
        'flow': 'accessCode',
        # 'redirect_uri': 'http://localhost/auth-response',
        'authorizationUrl': 'http://localhost:5000',
        'tokenUrl': 'https://localhost/token',
        'scopes': {
            'read': 'Grant read-only access',
            'write': 'Grant read-write access',
        }
    }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}