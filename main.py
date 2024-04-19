### ========== Library ========== ###
from fastapi import FastAPI
from routes.routes import router
import uvicorn

### ========== Create app instant ========== ###
app = FastAPI()

### ========== Include Route ========== ###
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
