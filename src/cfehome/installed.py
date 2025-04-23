DEFAULT_APPS = [
    # django-apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party-apps
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "slippers",
    "widget_tweaks",
]

# tenant/entreprise apps
_CUSTOMER_INSTALLED_APPS = DEFAULT_APPS + [
    # my-apps
    "commando",
    "profiles",
    "visits",
]

# public schema default installed apps
_INSTALLED_APPS = DEFAULT_APPS + [
    # my-apps
    "commando",
    "customers",
    "profiles",
    "subscriptions",
    "tenants",
    "visits",
]
