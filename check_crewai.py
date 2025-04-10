import inspect
import crewai

# Print all available modules and classes in crewai
print("Available in crewai package:")
for name, obj in inspect.getmembers(crewai):
    if not name.startswith("_"):  # Skip private attributes
        print(f"- {name}: {type(obj)}")