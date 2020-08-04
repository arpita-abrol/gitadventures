
from server import app
from flask import Response, request
from prometheus_client import generate_latest, Counter
from functools import wraps


@app.route('/metrics')
def promentheus_metrics():
    MIMETYPE = 'text/plain; version=0.0.4; charset=utf-8'
    return Response(generate_latest(), mimetype=MIMETYPE)


route_counter = Counter('requests_for_routes',
                        'Number of requests for specified routes',
                        ['method', 'endpoint'])


def track_requests(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        route_labels = {
            "method": request.method,
            "endpoint": str(request.path)
        }
        route_counter.labels(**route_labels).inc()
        return route(*args, **kwargs)
    return wrapper
