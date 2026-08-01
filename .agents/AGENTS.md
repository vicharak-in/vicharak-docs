# Documentation Update Rule

Whenever making modifications to the documentation (e.g. updating `.rst` or `.md` files):
1. Build the documentation locally to test your changes using the virtual environment:
   ```bash
   pipenv update
   pipenv run make html -j $(nproc --all)
   ```
2. Host the compiled HTML locally on a persistent background web server. **Use a persistent terminal (RunPersistent=true) with BypassSandbox=true** for this:
   ```bash
   python3 -m http.server 8000 -d _build/html
   ```
3. When making subsequent changes, **do not kill the server**. Instead, simply run `pipenv run make clean && pipenv run make html -j $(nproc --all)` in a standard command to rebuild the files. The persistent server will automatically serve the newly generated files.
4. Always inform the user that the recompilation is complete and they can preview the site at `http://localhost:8000`.

<RULE>
# Scope Restriction

When working on the Axon Lite documentation, **DO NOT** make any changes to files outside the `axon-lite` domain. Do not touch the main source files for other SBCs (but modifying index.rst to include axon-lite is allowed) (like `source/index.rst`) or any other SBC documentation folders (like `axon` or `vaaman`). Keep all modifications strictly confined to the `axon-lite` scope.
</RULE>
