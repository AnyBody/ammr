@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ=AMMRManual

if "%1" == "" goto help

if "%1" == "clean" goto clean

if "%1" == "release" goto release


%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The Sphinx module was not found. Make sure you have Sphinx installed,
	echo.then set the SPHINXBUILD environment variable to point to the full
	echo.path of the 'sphinx-build' executable. Alternatively you may add the
	echo.Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -n
robocopy /MIR _build\html ..\Documentation /mt /NFL /NDL /NJH /NJS /nc /ns /np
goto end


:release
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -n -W -t offline
robocopy /MIR _build\html ..\Documentation /mt /NFL /NDL /NJH /NJS /nc /ns /np
cd ..
git checkout -b archive
git checkout archive
git add -f Documentation\*
git commit -m "doc archive"
git archive archive -o release.zip
git reset --soft HEAD~
git reset
git checkout master
git branch -D archive
cd docs
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:clean
RMDIR /S /Q auto_examples
RMDIR /S /Q ..\Documentation
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:end
popd
