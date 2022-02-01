from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.users.decorators import login_required
from app.shortcuts import render, redirect


router = APIRouter(
    prefix='/videos'
)


@router.get("/create", response_class=HTMLResponse)
def video_create_view(request: Request):
    context = {}
    return render(request, "videos/create.html", context)


@router.get("/", response_class=HTMLResponse)
def video_list_view(request: Request):
    context = {}
    return render(request, "videos/list.html", context)



@router.get("/detail", response_class=HTMLResponse)
def video_detail_view(request: Request):
    return render(request, "videos/detail.html", {})