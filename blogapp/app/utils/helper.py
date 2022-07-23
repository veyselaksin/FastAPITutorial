from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def bcrypt(password: str):
        return password_context.hash(password)

def delete_dict_item(item: dict, keys: list, **kwargs):
    base_dict = dict([(key, value) for key, value in item.items() if key not in keys])
    
    if kwargs["is_sub_dict"]:
        sub_dict = dict([(key, value) for key, value in base_dict[kwargs["sub_dict"]].__dict__.items() if key not in keys])

    base_dict[kwargs["sub_dict"]] = sub_dict
    return base_dict