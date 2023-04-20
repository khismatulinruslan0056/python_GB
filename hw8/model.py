

def create(db: dict, id: int, surname: str, name: str, phone: str, discrip: str) -> dict:     #data_base
   db[id] = {'surname': surname, 'name': name, 'phone': phone, 'discrip':discrip}
   id += 1
   return db, id   


def read(db: dict, surname_filter: str) -> int: 
    for idx, data in db.items():
        if surname_filter.lower() in data['surname'].lower():
            return idx

def delete_line(db: dict, found_id: int) -> dict:
    del db[found_id]
    return db

def change_line(db: dict, found_id: int) -> dict:
    for val in db[found_id]:
        print(f'{val}: ')
        new_value = input()
        if len(new_value) > 0:
            db[found_id][val] = new_value
    return db