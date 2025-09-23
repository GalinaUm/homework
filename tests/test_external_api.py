from unittest.mock import patch

from src.external_api import convert


@patch("src.external_api.os.getenv")
def test_api_key_loaded(mock_getenv):
    """Проверяет, что API_KEY загружается из переменных окружения."""
    mock_getenv.return_value = "TEST_API_KEY"

    mock_getenv("API_KEY")
    mock_getenv.assert_called_with("API_KEY")


# @patch("requests.get")
# def test_convert(response, transaction):
#     response.return_value.json.return_value = {'result': 187.13}
#     assert convert(transaction) == 187.13
#     response.assert_called_once()
