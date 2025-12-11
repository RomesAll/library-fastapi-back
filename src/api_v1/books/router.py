from fastapi import APIRouter

router = APIRouter(prefix='/books', tags=['Books',])

@router.get('/all')
async def get_all_books():
    pass

@router.get('/{book_id}')
async def get_book_by_id(book_id):
    pass

@router.post('/create')
async def create_book():
    pass

@router.patch('/update')
async def update_book():
    pass

@router.delete('/delete')
async def delete_book():
    pass