from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"
    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"

    with pytest.raises(TypeError) as exception:
        encrypt_message("AABBCC", "key_invalida")
    assert exception.value.args[0] == "tipo inválido para key"
    assert exception.type == TypeError

    with pytest.raises(TypeError) as exception:
        encrypt_message(123456, 3)
    assert exception.value.args[0] == "tipo inválido para message"
    assert exception.type == TypeError
