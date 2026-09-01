from fastapi import FastAPI
from routes.chamado_routes import router as chamado_router

app = FastAPI(title="API de Chamados")

app.include_router(chamado_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)