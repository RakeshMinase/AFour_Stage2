# from resources.user import UserRegister
# from models import user
from app import app

app = app()


def test_register():
    with app.test_client() as c:
        response = c.post("/login", json={"username": "varun", "password": "123"})
        # json_response = response.get_json()
        assert response.status_code == 200


# def test_can_register(client):
#     response = client.post("/register", json={"username": "rakesh", "password": "123"})
#     print("------------------")
#     print(response)

    # assert user.query.count() == 1
