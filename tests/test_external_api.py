from unittest.mock import patch


@patch("src.external_api.os.getenv")
def test_api_key_loaded(mock_getenv):
    """Проверяет, что API_KEY загружается из переменных окружения."""
    mock_getenv.return_value = "TEST_API_KEY"

    mock_getenv("API_KEY")
    mock_getenv.assert_called_with("API_KEY")
