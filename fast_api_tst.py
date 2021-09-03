from fastapi import FastAPI, Request, Form
from typing import List
from fastapi.templating import Jinja2Templates

dct = {"ctp_a": 1,
       "ctp_b": 2,
       "ctp_c": 20,
       "ctp_d": 4
       }

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/form")
def form_post_init(request: Request):
    result = dct
    return templates.TemplateResponse(
        'form.html',
        context={'request': request, 'multiply_by': 2, 'result': result}
        )

@app.post("/form")
def form_post_modif(
        request: Request,
        multiply_by: int = Form(...),
        ctp_names: List[str] = Form(...),
        values: List[int] = Form(...)
        ):
    
    result = dict(zip(ctp_names, [v*multiply_by for v in values]))

    return templates.TemplateResponse(
        'form.html',
        context={'request': request, 'multiply_by': multiply_by, 'result': result}
        )
