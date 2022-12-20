def _generate_email(email, oauth_type, user_id):
    if not email:
        email = f'{oauth_type}{user_id}@project.dummy.address'

    return email

def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = {
        'username': details.get('username'),
        'email':    _generate_email(details.get('email'), backend.name, kwargs.get('uid')),
        'viewname': details.get('username'),
    }

    return {
        'is_new': True,
        'user': strategy.create_user(**fields),
    }