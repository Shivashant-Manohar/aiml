import random
def split_data(data,prob):
    results = [],[]
    for row in data:
        results [0 if random.random() < prob else 1].append(row)
    return results

def test_train_split( x,y,test_pct ):
    data = list(zip(x,y))
    train , test = split_data(data,1-test_pct)
    if not train or not test:
        split_index = int(len(data) * (1 - test_pct))
        train = data[:split_index]
        test = data[split_index:]
    x_train, y_train = zip(*train)
    x_test , y_test = zip(*test)
    return x_train,x_test,y_train,y_test

hours_studied = [10, 20, 5, 8, 15, 2, 25, 12]
exam_scores   = [85, 95, 60, 72, 90, 50, 98, 88]

x_train, x_test, y_train, y_test = test_train_split(hours_studied, exam_scores,0.3)
print("--- Training Set ---")
print(f"Features (x_train): {x_train}")
print(f"Labels   (y_train): {y_train}")
print("\n--- Test Set ---")
print(f"Features (x_test): {x_test}")
print(f"Labels   (y_test): {y_test}")




