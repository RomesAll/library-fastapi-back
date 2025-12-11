from fastapi import APIRouter

router = APIRouter(prefix='/client', tags=['Client',])

@router.get('/all')
async def get_all_client():
    pass

@router.get('/{client_id}')
async def get_client_by_id(client_id):
    pass

@router.post('/create')
async def create_client():
    pass

@router.patch('/update')
async def update_client():
    pass

@router.delete('/delete')
async def delete_client():
    pass