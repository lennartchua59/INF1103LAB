"""Runs every Week 10 test script. Used by: docker run <image> python run_all_tests.py"""
import runpy

for script in ("test_association.py", "test_aggregation.py",
               "test_composition.py", "test_lsp_polymorphism.py"):
    print("\n" + "=" * 60)
    print("RUNNING", script)
    print("=" * 60)
    runpy.run_path(script)
