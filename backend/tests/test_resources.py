"""
Set of tests for backend.application.resources
"""
import json


def test_get_usage_stamp(client, mocker):
    mocked_usage_stamp = {'current_month_download': '10.5',
                          'current_month_upload': '4.0',
                          'time_stamp': 'Sun, 29 May 2022 14:22:34 GMT'}

    mock_get_newest_by_date = mocker.patch('backend.application.models.UsageStamp.get_newest_by_date',
                                           return_value=mocked_usage_stamp)
    response = client.get('/api/usage-stamp/')
    mock_get_newest_by_date.assert_called_once()
    assert response.status_code == 200
    assert mocked_usage_stamp == json.loads(response.get_data(as_text=True))


def test_get_usage_stamp_without_usage_stamps(client, mocker):

    mock_get_newest_by_date = mocker.patch('backend.application.models.UsageStamp.get_newest_by_date',
                                           return_value=None)
    response = client.get('/api/usage-stamp/')
    mock_get_newest_by_date.assert_called_once()
    assert response.status_code == 200
    assert None == json.loads(response.get_data(as_text=True))


def test_put_usage_stamp(client, mocker):
    mocked_usage_stamp = {'current_month_download': '10.5',
                          'current_month_upload': '4.0',
                          'time_stamp': 'Sun, 29 May 2022 14:22:34 GMT'}
    mock_db_session_add = mocker.patch('backend.application.extensions.db.session.add')
    mock_db_session_commit = mocker.patch('backend.application.extensions.db.session.commit')
    
    response = client.put('/api/usage-stamp/', query_string=mocked_usage_stamp)
    mock_db_session_add.assert_called_once()
    mock_db_session_commit.assert_called_once()
    assert response.status_code == 200
    assert mocked_usage_stamp == json.loads(response.get_data(as_text=True))


def test_put_usage_stamp_bad_request(client, mocker):
    mocked_usage_stamp = {'current_month_download': None,
                          'current_month_upload': '4.0',
                          'time_stamp': 'Sun, 29 May 2022 14:22:34 GMT'}
    mock_db_session_add = mocker.patch('backend.application.extensions.db.session.add')
    mock_db_session_commit = mocker.patch('backend.application.extensions.db.session.commit')
    
    response = client.put('/api/usage-stamp/', query_string=mocked_usage_stamp)
    mock_db_session_add.assert_not_called()
    mock_db_session_commit.assert_not_called()
    assert response.status_code == 400
    assert b'Bad request - missing parameter' in response.data


def test_get_usage_stamps(client, mocker):
    mocked_usage_stamp_1 = {'current_month_download': '10.5',
                            'current_month_upload': '4.0',
                            'time_stamp': 'Sun, 29 May 2022 14:22:34 GMT'}
    mocked_usage_stamp_2 = {'current_month_download': '11.5',
                            'current_month_upload': '4.0',
                            'time_stamp': 'Sun, 29 May 2022 14:26:34 GMT'}

    mock_get_multiple_newest_by_date = mocker.patch('backend.application.models.UsageStamp.get_multiple_newest_by_date',
                                           return_value=[mocked_usage_stamp_1, mocked_usage_stamp_2])
    response = client.get('/api/usage-stamps/')
    mock_get_multiple_newest_by_date.assert_called_once()

    assert response.status_code == 200
    assert len(json.loads(response.get_data(as_text=True))) == 2
    assert mocked_usage_stamp_1 == json.loads(response.get_data(as_text=True))[0]


def test_get_usage_stamps_without_usage_stamps(client, mocker):
    mock_get_multiple_newest_by_date = mocker.patch('backend.application.models.UsageStamp.get_multiple_newest_by_date',
                                           return_value=[])
    response = client.get('/api/usage-stamps/')
    mock_get_multiple_newest_by_date.assert_called_once()

    assert response.status_code == 200
    assert len(json.loads(response.get_data(as_text=True))) == 0

