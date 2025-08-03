import random

def split_data(data, prob):
    """Splits data into two fractions [prob, 1 - prob]"""
    # 1. Initialize two empty lists to store the results.
    results = [], []
    
    # 2. Loop through each item in the input list 'data'.
    for row in data:
        # 3. For each item, decide which list to put it in.
        #    - random.random() generates a number between 0.0 and 1.0.
        #    - If this number is less than 'prob', the item goes into results[0].
        #    - Otherwise, it goes into results[1].
        results[0 if random.random() < prob else 1].append(row)
        
    # 4. Return the two new lists.
    return results

def train_test_split(x, y, test_pct):
    """
    Splits features x and labels y into training and testing sets.
    """
    # 1. Pair corresponding x and y values into a single list of tuples.
    #    Example: [(x1, y1), (x2, y2), ...]
    data = list(zip(x, y))
    
    # 2. Use the helper function to split the list of pairs.
    #    The probability for the training set is (1 - test_pct).
    train, test = split_data(data, 1 - test_pct)
    
    # 3. Handle a rare edge case where a small dataset might result in an empty list.
    if not train or not test:
        split_index = int(len(data) * (1 - test_pct))
        train = data[:split_index]
        test = data[split_index:]

    # 4. "Unzip" the pairs back into separate lists for features and labels.
    #    The '*' operator unpacks the list of tuples for zipping.
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    
    # 5. Return the four final datasets.
    return x_train, x_test, y_train, y_test

# --- Example Usage ---

# 1. Define the raw data: features (x) and labels (y).
hours_studied = [10, 20, 5, 8, 15, 2, 25, 12]
exam_scores   = [85, 95, 60, 72, 90, 50, 98, 88]

# 2. Call the main function to perform the split.
#    We want 30% of the data for the test set.
#    The four returned lists are assigned to four variables.
x_train, x_test, y_train, y_test = train_test_split(hours_studied, exam_scores, 0.3)

# 3. Print the final separated datasets to see the result.
print("--- Training Set ---")
print(f"Features (x_train): {x_train}")
print(f"Labels   (y_train): {y_train}")
print("\n--- Test Set ---")
print(f"Features (x_test): {x_test}")
print(f"Labels   (y_test): {y_test}")