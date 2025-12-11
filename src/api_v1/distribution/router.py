from fastapi import APIRouter

router = APIRouter(prefix='/distribution', tags=['Distribution',])

@router.get('/all')
async def get_all_distribution():
    pass

@router.get('/{distribution_id}')
async def get_distribution_by_id(distribution_id):
    pass

@router.post('/create')
async def create_distribution():
    pass

@router.patch('/update')
async def update_distribution():
    pass

@router.delete('/delete')
async def delete_distribution():
    pass