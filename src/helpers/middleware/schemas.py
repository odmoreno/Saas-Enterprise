class SchemaTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        host = request.get_host()
        host_portless = host.split(":")[0]
        host_split = host_portless.split(".")
        subdomain = None
        if len(host_split) > 1:
            subdomain = host_split[0]
        print("Host:", host, request.scheme, host_split, subdomain)
        schema_name = self.get_schema_name(subdomain=subdomain)
        self.set_search_path(schema_name)
        return self.get_response(request)

    def set_search_path(self, schema_name):
        print("activate the schema", schema_name)
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO "{schema_name}";')
            print(f"Search path set to {schema_name}")

    def get_schema_name(self, subdomain=None):
        if subdomain is None:
            return "public"
        if subdomain == "localhost":
            return "public"
        if subdomain == "cfe":
            return "example"
        return
