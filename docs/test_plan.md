# Test Plan
1. **Unit Testing**: Pytest for `/health`, `/ready`, and `/predict` validation.
2. **Integration Testing**: Verify Docker containers talk to each other (Frontend -> API).
3. **Pipeline Testing**: GitHub Actions runs `orchestrator.py` to ensure training doesn't crash on standard environments.