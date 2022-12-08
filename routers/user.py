from fastapi import APIRouter

from schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

mock_users = [{
    "id": "skfhshdxsdsdvfhktjr3edfdsvbs",
    "email": "enelipax@gmail.com",
    "username": "Rick",
    "password": "**********"
}, {
    "id": "skfhshdxv464565fhktjr3edfdsvbs",
    "email": "enelipaz@gmail.com",
    "username": "Morty",
    "password": "**********"
}]


@router.get("/")
async def get_users():
    return mock_users


@router.post("/create", response_model=User)
async def create_user(user: User):
    user.id = "skfhshdxvfhktjr3edfdsvbs"
    return user


# @router.get("/me")
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/{username}")
# async def read_user(username: str):
#     return {"username": username}
