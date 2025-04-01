import pytest
from app.main import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        "password,is_valid",
        [
            pytest.param(
                "A5@bc",
                False,
                id="password has less than 8 characters"
            ),
            pytest.param(
                "A5@bcdefghijklmnop",
                False,
                id="password has more than 16 characters"
            ),
            pytest.param(
                "abc5_efgh",
                False,
                id="password has no uppercase"
            ),
            pytest.param(
                "Alexcyberf@",
                False,
                id="password has no digit"
            ),
            pytest.param(
                "Alexcyberf5",
                False,
                id="password has no special symbol"
            ),
            pytest.param(
                "Abcdefg5!",
                True,
                id="password has all needed rules"
            ),
        ]
    )
    def test_password(self,password: str, is_valid: bool) -> None:
        assert check_password(password) is is_valid
