from model import Usuario


def get_all_users():
    return Usuario.query().order(Usuario.nome)


def get_user_by_email(email):
    return Usuario.query(Usuario.email == email)


def add_user(name, email, google_id=None):
    if google_id:
        user = Usuario(nome=name, google_id=google_id, email=email)
        return user
    user = Usuario(nome=name, email=email)
    return user

def edit_user(name, email, google_id):
    user = Usuario.query(Usuario.google_id == google_id).get()
    if user:
        user.nome = name
        user.email = email
        user.put()

