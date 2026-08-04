from signal_processing.loader import load_radioml

dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

print(type(dataset))
print()

print("Total Keys:", len(dataset))

print()

print("First 10 Keys:")

for i, key in enumerate(dataset.keys()):
    print(key)

    if i == 9:
        break