from fastapi import FastAPI
from config import session_factory, session_factory
from sqlalchemy import text
import uvicorn

app = FastAPI()

@app.get('/test-db')
async def testing_db():
    async with session_factory() as session:
        query = text("SELECT VERSION()")
        result = await session.execute(query)
        return result.scalars().all()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)