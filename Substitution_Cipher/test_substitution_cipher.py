from substitution_cipher import SubMessage, EncryptedSubMessage

def test_build_transpose_dict():
    test_parameter = "Hello"
    
    msg1 = SubMessage(test_parameter)
    assert msg1.build_transpose_dict("eaiuo") == {
        'A': 'E', 'E': 'A', 'I': 'I', 'O': 'U', 'U': 'O', 
        'a': 'e', 'e': 'a', 'i': 'i', 'o': 'u', 'u': 'o'
        }
    
    msg2 = SubMessage(test_parameter)
    assert msg2.build_transpose_dict("oaeui") == {
        'A': 'O', 'E': 'A', 'I': 'E', 'O': 'U', 'U': 'I', 
        'a': 'o', 'e': 'a', 'i': 'e', 'o': 'u', 'u': 'i'
        }
    
    msg3 = SubMessage(test_parameter)
    assert msg3.build_transpose_dict("iuaeo") == {
        'A': 'I', 'E': 'U', 'I': 'A', 'O': 'E', 'U': 'O',
        'a': 'i', 'e': 'u', 'i': 'a', 'o': 'e', 'u': 'o'
        }
    
    
def test_apply_transpose():
    msg1 = SubMessage("Hello World!")
    enc_dict1 = msg1.build_transpose_dict("eaiuo")
    assert msg1.apply_transpose(enc_dict1) == "Hallu Wurld!"
    
    msg2 = SubMessage("The Third")
    enc_dict2 = msg2.build_transpose_dict("oaeui")
    assert msg2.apply_transpose(enc_dict2) == "Tha Therd"
    
    msg3 = SubMessage("One of the greatest!")
    enc_dict3 = msg3.build_transpose_dict("iuaeo")
    assert msg3.apply_transpose(enc_dict3) == "Enu ef thu gruitust!"
    

def test_decrypt_message():
    enc_msg1 = EncryptedSubMessage("Hallu Wurld!")
    assert enc_msg1.decrypt_message() == "Hello World!"
    
    enc_msg2 = EncryptedSubMessage("Tha Therd")
    assert enc_msg2.decrypt_message() == "The Third"
    
    enc_msg3 = EncryptedSubMessage("Enu ef thu gruitust!")
    assert enc_msg3.decrypt_message() == "One of the greatest!"