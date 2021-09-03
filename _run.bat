set root=C:\Users\novotny\Documents\Anaconda3

call %root%\Scripts\activate.bat %root%

start chrome http://127.0.0.1:8000/form

call uvicorn fast_api_tst:app --reload

pause