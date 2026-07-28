from fastapi import APIRouter

router = APIRouter(
    prefix="/main",
    tags=["Main Route"]
)
@router.get("/")
async def hello_world():
    return {'message': "Hello World"}