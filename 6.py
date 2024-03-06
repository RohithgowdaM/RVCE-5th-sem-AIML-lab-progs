def calculate_mean(feature_values):
    return sum(feature_values) / len(feature_values)

def calculate_std_dev(feature_values, mean):
    variance = sum((x - mean) ** 2 for x in feature_values) / len(feature_values)
    return variance ** 0.5

def calculate_probability(x, mean, std_dev):
    exponent = -(x - mean) ** 2 / (2 * std_dev ** 2)
    return (2.71828 ** exponent) / (std_dev * (2 * 3.14159) ** 0.5)

def fit(X, y):
    num_instances, num_features = len(X), len(X[0])
    class_probabilities = {}
    mean_and_std_dev = {}

    # Calculate class probabilities
    for label in set(y):
        class_probabilities[label] = sum(1 for value in y if value == label) / num_instances

    # Calculate mean and standard deviation for each feature in each class
    for label in set(y):
        indices = [i for i, value in enumerate(y) if value == label]
        mean_and_std_dev[label] = {}
        for feature in range(num_features):
            feature_values = [X[i][feature] for i in indices]
            mean_and_std_dev[label][feature] = {
                'mean': calculate_mean(feature_values),
                'std_dev': calculate_std_dev(feature_values, calculate_mean(feature_values))
            }

    return class_probabilities, mean_and_std_dev

def predict(X, class_probabilities, mean_and_std_dev):
    predictions = []
    probabilities = []
    for instance in X:
        instance_probabilities = {}
        for label, class_prob in class_probabilities.items():
            instance_probabilities[label] = class_prob
            for feature, value in enumerate(instance):
                mean = mean_and_std_dev[label][feature]['mean']
                std_dev = mean_and_std_dev[label][feature]['std_dev']
                instance_probabilities[label] *= calculate_probability(value, mean, std_dev)

        predicted_label = max(instance_probabilities, key=instance_probabilities.get)
        predictions.append(predicted_label)
        probabilities.append(instance_probabilities[predicted_label])

    return predictions, probabilities

# Additional Information about the Iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
print("Dataset Information:")
print("Name of the dataset: Iris")
print("Number of features:", iris.data.shape[1])
print("Number of instances:", iris.data.shape[0])
print("All features are numerical.")
print("Number of numerical features:", iris.data.shape[1])
print("Number of categorical features: 1")
print("Name of the Target variable: Species")

# Binary classification for Iris-Virginica
y_binary = (iris.target == 2).astype(int)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, y_binary, test_size=0.2, random_state=42)

# Train the model
class_probabilities, mean_and_std_dev = fit(X_train, y_train)

# Make predictions on the test data
predictions, probabilities = predict(X_test, class_probabilities, mean_and_std_dev)

# Display predictions along with true labels and probabilities
result = list(zip(predictions, probabilities, y_test))
print("\nPredictions:")
print("Predicted | Probability | Actual")
print("-----------------------------")
for pred, prob, actual in result:
    print(f"    {pred}    |     {prob:.4f}     |    {actual}")

# Evaluate the accuracy or other metrics based on your task
accuracy = sum(pred == true_label for pred, true_label in zip(predictions, y_test)) / len(y_test)
print(f'\nAccuracy: {accuracy}')
