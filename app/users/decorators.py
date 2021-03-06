from functools import wraps
from logging import exception
from fastapi import Request, HTTPException

from .auth import verify_user_id
from app.users.exceptions import LoginRequiredException

def login_required(func):
    @wraps(func)
    def wrapper(request: Request, *args, **kwargs):
        # session_token = request.cookies.get('session_id')
        # user_session = verify_user_id(session_token)
        # if user_session is None:
        if not request.user.is_authenticated:
            raise LoginRequiredException(status_code=400)
        return func(request, *args, **kwargs)
    return wrapper