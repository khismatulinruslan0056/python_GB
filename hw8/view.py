def record_id(db: dict, idx:int) -> None:
    print(f'{db[idx]}')

def print_db(db: dict) -> None:
    for idx, data in db.items():
        print(f"[{idx}: {data['surname']} | {data['name']} | {data['phone']} | {data['discrip']}]")        