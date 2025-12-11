from fastapi import APIRouter

router = APIRouter(prefix='/reservation', tags=['Reservation',])

@router.get('/all')
async def get_all_reservation():
    pass

@router.get('/{reservation_id}')
async def get_reservation_by_id(reservation_id):
    pass

@router.post('/create')
async def create_reservation():
    pass

@router.patch('/update')
async def update_reservation():
    pass

@router.delete('/delete')
async def delete_reservation():
    pass