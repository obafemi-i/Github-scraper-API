from fastapi import FastAPI
from extract import Extract


app = FastAPI()
scrape = Extract()


@app.get('/{id}')
async def details(id):
    return scrape.get_deets(id)      
    
