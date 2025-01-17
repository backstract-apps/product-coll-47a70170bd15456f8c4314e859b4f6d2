from fastapi import FastAPI, Request
from database import engine
from prometheus_client import Counter, Histogram, Gauge, make_asgi_app
from starlette.middleware.wsgi import WSGIMiddleware
import models
import uvicorn
from routes import router
import time

# Database setup
models.Base.metadata.create_all(bind=engine)

# Prometheus core metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency', ['method', 'endpoint', 'http_status'])
IN_PROGRESS = Gauge('http_requests_in_progress', 'HTTP requests in progress')

app = FastAPI(title='Backstract Generated APIs - product-coll-47a70170bd15456f8c4314e859b4f6d2',debug=False,docs_url='/tender-galois-62a4edf8d04611ef96b90242ac12000246/docs',openapi_url='/tender-galois-62a4edf8d04611ef96b90242ac12000246/openapi.json')

app.include_router(router, prefix='/tender-galois-62a4edf8d04611ef96b90242ac12000246/api', tags=['APIs v1'])

# Middleware for Prometheus metrics
@app.middleware('http')
async def prometheus_middleware(request: Request, call_next):
    method = request.method
    path = request.url.path
    start_time = time.time()

    IN_PROGRESS.inc()  # Increment in-progress requests

    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception as e:
        status_code = 500  # Internal server error
        raise e
    finally:
        duration = time.time() - start_time
        REQUEST_COUNT.labels(method=method, endpoint=path, http_status=status_code).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=path, http_status=status_code).observe(duration)
        IN_PROGRESS.dec()  # Decrement in-progress requests

    return response

# Prometheus metrics endpoint
prometheus_app = make_asgi_app()
app.mount('/metrics', prometheus_app)

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=7070, reload=True)

if __name__ == '__main__':
    main()

