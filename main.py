from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from tqdm import tqdm

dt_now = datetime.now()

def loading():
    for i in tqdm(range(10000000)):
        pass

if __name__ == '__main__':
    print(dt_now)
    get_employees()
    calculate_salary()
    loading()
