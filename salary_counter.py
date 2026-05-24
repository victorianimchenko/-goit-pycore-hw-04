# TASK 1


from pathlib import Path

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                name, salary = line.split(",")
                total +=int(salary)
                count +=1

        average = total/count if count >0 else 0
        return total, average
    
    except (FileNotFoundError, ValueError):
        return 0, 0


file_path = Path(__file__).parent / "salary.txt"
total, average = total_salary(file_path)
print(f"Total amount: {total}, Average amount: {average:.0f}")



# TASK2


def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                    
                    })
                
        return cats
            

    except Exception as e:
        print("Eroro", e)

    
path_cats = Path(__file__).parent / "cats.txt"

if path_cats.exists():
    print(f"{path_cats} існує")
cats_info = get_cats_info(path_cats)
print(cats_info)

    







