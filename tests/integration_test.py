import requests
import pytest
import psycopg2


def test_youtube_api_response(airflow_variable):
    api_key = airflow_variable("api_key")
    channel_handle = airflow_variable("channel_handle")

    url = "https://www.googleapis.com/youtube/v3/channels"

    params = {
        "part": "contentDetails",
        "forHandle": channel_handle,
        "key": api_key
    }

    response = requests.get(url, params=params, timeout=15)

    assert response.status_code == 200, (
        f"YouTube API error: {response.text}"
    )


def test_real_postgres_connection(real_postgres_connection):
    cursor = None

    try:
        cursor = real_postgres_connection.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()

        assert result[0] == 1

    except psycopg2.Error as e:
        pytest.fail(f"Database query failed: {e}")

    finally:
        if cursor is not None:
            cursor.close()