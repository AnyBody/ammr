# Contribute to Model Development

The Model Repository is the product of collaboration between AnyBody Technology,
and many academic institutions and research projects.

If you are interested in beta models/repositories you can get access to the
development version of the AMMR on GitHub. Development happens on GitHub
where you can follow the development and contribute to the models. All 
contributions are welcome and greatly appreciated.

If you find a bug or have comments to the code please report it on the 
[AnyScript forum](https://forum.anyscript.org).

If you have a fix or an improvement to the models we are happy to accept it. Code contributions and 
fixes are submitted through [pull requests]() on GitHub. 

Simply fork the repository on GitHub, edit your fork and [start a pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 

You can also view other freely available models and resources hosted on [GitHub](https://github.com/anybody).

:::{only} draft
```{rubric} Release checklist
```

\# Update `AMMR.version.any`.

> \# Update with the new version numbers
>
> \# Fill the `ANYBODY_HASH_BODY`. The new value can be found in `Main.HumanModel.Config.HashBodyModel`.

\# Update any  AMS version number in `Docs/conf.py` (only used when building locally)

\# Create new version of AMMR on Zenodo (<https://zenodo.org/record/3404750>).

> \# Click `New version` button
>
> \# Fill the neccessary fields. Authors are those who contributed since last Release
>
> \# Note the draft DOI which zenodo reserves
>
> \# Save the draft but do **not** publish it.

\# Clean up, and update `Docs/changelog.rst`

> \# Prof read and check that all changes are documented.
>
> \# Add Zenodo DOI url to the new release, and fill the date

\# Check that the docs can build, and that the tests pass.

\# Merge the branch and add a git tag.

\# Upload ammr zip file to Zenodo

> \# Either use the AMMR zip file created by the AMS build. This  (it con or create a
>
> : released zip file by running:
>
>   ```
>   cd Docs
>   make release
>   mv release.zip ammr-X.Y.Z.zip
>   ```
>
>   This creates a zip file with the built documentation.
>
> \# Edit the draft Zenodo release to upload a zip file with AMMR.



:::
