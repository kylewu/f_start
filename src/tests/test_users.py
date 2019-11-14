def test_post_user(client):
    res = client.post('/users', json={'handle': 'wenbin'})
    assert res.status_code == 401

    res = client.post('/users', headers={'Authorization': 'admin'}, json={'handle': 'wenbin'})
    assert res.status_code == 201

    assert res.json['handle'] == 'wenbin'


def test_get_user(client):
    res = client.get('/users')
    assert res.status_code == 200

    assert len(res.json['results']) > 0
