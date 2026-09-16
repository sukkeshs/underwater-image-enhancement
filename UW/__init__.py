import os

# Allow legacy imports like `UW.core.*` to resolve to repo-root packages.
__path__.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
