from fastapi import FastAPI

app = FastAPI()


@app.get('/name')
async def my_first_end_point():
    return {'name': 'Abdul-Mumin',
            'father': 'Rufai Bawa',
            'mother': 'Rukayatu Yakubu'
            }
