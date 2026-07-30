from pwdlib import PasswordHash

senha_hash = PasswordHash.recommended()
print(senha_hash.hash("123456"))