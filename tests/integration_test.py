def test_youtube_api_response(airflow_variable):
    api_key = airflow_variable("api_key")
    channel_handle = airflow_variable("channel_handle")

    assert api_key is not None, "API key was not loaded"
    assert channel_handle is not None, "Channel handle was not loaded"

    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={api_key}"

    response = requests.get(url)

    print("STATUS CODE:", response.status_code)
    print("YOUTUBE RESPONSE:", response.text)

    assert response.status_code == 200