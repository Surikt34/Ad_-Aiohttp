from aiohttp import web
from models import ads, Ad


async def create_ad(request):
    data = await request.json()
    if 'title' not in data or 'description' not in data or 'owner' not in data:
        return web.json_response({'error': 'Invalid input'}, status=400)

    new_ad = Ad(
        title=data['title'],
        description=data['description'],
        owner=data['owner']
    )
    ads.append(new_ad)

    return web.json_response({'message': 'Объявление успешно создано', 'ad': new_ad.to_dict()}, status=201)


async def get_ad(request):
    ad_id = int(request.match_info['ad_id'])
    if 0 <= ad_id < len(ads):
        ad = ads[ad_id]
        return web.json_response(ad.to_dict())
    else:
        return web.json_response({'error': 'Ad not found'}, status=404)


async def delete_ad(request):
    ad_id = int(request.match_info['ad_id'])
    if 0 <= ad_id < len(ads):
        deleted_ad = ads.pop(ad_id)
        return web.json_response({'message': 'Объявление удалено', 'ad': deleted_ad.to_dict()})
    else:
        return web.json_response({'error': 'Ad not found'}, status=404)


app = web.Application()
app.add_routes([web.post('/ads', create_ad)])
app.add_routes([web.get(r'/ads/{ad_id:\d+}', get_ad)])
app.add_routes([web.delete(r'/ads/{ad_id:\d+}', delete_ad)])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)