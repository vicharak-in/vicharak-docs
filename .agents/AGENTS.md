# Documentation Update Rule

Whenever making modifications to the documentation (e.g. updating `.rst` or `.md` files):
1. Build the documentation locally to test your changes using the virtual environment:
   ```bash
   pipenv update
   pipenv run make html -j $(nproc --all)
   ```
2. Host the compiled HTML locally on a background web server. **Note: Always run the Python HTTP server with BypassSandbox set to true (unsandboxed), otherwise the host browser cannot access the port.**
   ```bash
   cd _build/html
   python3 -m http.server 8000
   ```
3. Always inform the user that the recompilation is complete and they can preview the site at `http://localhost:8000`.

**Note: Ensure you stop hosting, rebuild, and rehost after each change.**

<RULE>
# Scope Restriction

When working on the Axon Lite documentation, **DO NOT** make any changes to files outside the `axon-lite` domain. Do not touch the main source files for other SBCs (but modifying index.rst to include axon-lite is allowed) (like `source/index.rst`) or any other SBC documentation folders (like `axon` or `vaaman`). Keep all modifications strictly confined to the `axon-lite` scope.
</RULE>
