from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="protected_app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"request": request}
    )


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request, "message": None}
    )


@app.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    # Deliberately insecure demo behavior for testing WAF
    if "'" in username or "'" in password or "or 1=1" in username.lower() or "or 1=1" in password.lower():
        message = f"Suspicious login attempt detected in demo input: {username}"
    else:
        message = f"Demo login attempt received for user: {username}"

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request, "message": message}
    )


@app.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, q: str = ""):
    # Reflect query for XSS demo testing
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={"request": request, "query": q}
    )


@app.get("/comment", response_class=HTMLResponse)
async def comment_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="comment.html",
        context={"request": request, "message": None}
    )


@app.post("/comment", response_class=HTMLResponse)
async def comment_submit(request: Request, comment: str = Form(...)):
    # Reflect comment for XSS demo testing
    return templates.TemplateResponse(
        request=request,
        name="comment.html",
        context={"request": request, "message": comment}
    )


@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"request": request}
    )