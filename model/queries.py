from model.File import File


def get_files_for_user(user):
    return File.query(File.user == user).fetch()