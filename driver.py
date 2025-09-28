import importlib.util
import os
import sys

ROOT = os.path.dirname(__file__)
MODULES = ["00_navigation", "01_basics", "02_control_flow", "03_data_structures","04_classes_and_methods"]
TESTS_DIR = os.path.join(ROOT, "tests")


def load_module(path, name="exercise"):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run_exercises():
    for module in MODULES:
        print(f"\n=== Checking {module} ===")
        folder = os.path.join(ROOT, module)
        exercises = sorted(f for f in os.listdir(folder) if f.endswith(".py"))

        for ex in exercises:
            path = os.path.join(folder, ex)

            # Check for REMOVE line
            with open(path) as f:
                first_line = f.readline().strip()

            # Load learners code
            learner_mod = load_module(path, name="exercise")

            # Load matching test
            test_file = f"test_{module}_{ex}"
            test_path = os.path.join(TESTS_DIR, test_file)

            if not os.path.exists(test_path):
                print(f" No test found for {ex}")
                continue

            test_mod = load_module(test_path, name="test")

            try:
                test_mod.run(learner_mod)
                print(f" {ex} passed!")
            except AssertionError as e:
                print(f" {ex} failed. Details: {e}")
                return
            except Exception as e:
                print(f" {ex} crashed: {e}")
                return

            # If this exercise had REMOVE line, stop here
            if "REMOVE THIS TO MOVE ON" in first_line:
                print(f" Module Passed! Remove the \"# REMOVE TO MOVE ON\" banner to continue")
                return

        print(f" {module} complete!")

    print("\n All modules finished!")


if __name__ == "__main__":
    run_exercises()
