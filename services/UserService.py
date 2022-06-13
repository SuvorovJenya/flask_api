def get_by_username_password(
    username: str,
    password: str,
    db: Session = Depends(get_db),
):
    # services/users.getById
    user = get_user(db, username)
    if not user:
        return False
    return user
