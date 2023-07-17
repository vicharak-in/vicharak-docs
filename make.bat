@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation


set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=_build

if "%VIRTUAL_ENV%" == "" (
    del Pipfile.lock
	python -m pipenv update
	python -m pipenv shell

	goto end
)

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help
if "%1" == "spelling" goto spelling

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:spelling
echo "Spellchecker is disabled for windows"
echo "https://github.com/pyenchant/pyenchant/issues/306"
goto end
%SPHINXBUILD% -b spelling %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
if not "%VIRTUAL_ENV%" == "" (
	exit /b 0
)
popd
