from flask import Flask, request, jsonify
import requests
import redis

from flask_caching import Cache


# def create_app():
app = Flask(__name__)

app.config.from_object("config")

app.config["CACHE_TYPE"] = "RedisCache"
# app.config["CACHE_REDIS_HOST"] = "localhost"
# app.config["CACHE_REDIS_PORT"] = 6379
# app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

cache = Cache(app)

db = redis.Redis(host="redis_container", port=6379, decode_responses=True)
# db.init_app(app)


@app.route("/universities")
@cache.cached(timeout=3000, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get("country")
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

    # return app


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello World"


# if __name__ == "__main__":
#     app.run()
