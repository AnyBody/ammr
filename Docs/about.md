# About the AnyBody Model Repository

## Cite 

The AnyBody Managed Model Repository has a DOI {{ DOI }}. This is handled by
[Zenodo.org](https://zenodo.org/), which is an European Open Science platform
hosted at CERN. You can download all archived versions of the AMMR from
[Zenodo.org](https://doi.org/10.5281/zenodo.1250764).

You can download all archived versions of the AMMR from
[Zenodo.org](https://doi.org/10.5281/zenodo.1250764). The DOI is useful when
citing the a specific version of the AMMR. For example, when citing the AMMR
2.4.3:

:::{note}
:class: margin
Remember to use the DOI for the specific version you use.
:::

:::{card} {material-regular}`format_quote;2em;` Citation
Lund, Morten Enemark, Tørholm, Søren, et al. (2023, Jan 29). The AnyBody Managed 
Model Repository (AMMR) (Version 2.4.3). Zenodo. <https://doi.org/10.5281/zenodo.7572879>
:::


## Contribute

The Model Repository is the product of collaboration between AnyBody Technology,
and many academic institutions and research projects. Development happens on GitHub
where you can follow the development and contribute to the models.

All contributions are welcome and greatly appreciated. If you find a bug or have 
comments to the code please report it on the [AnyScript forum](https://forum.anyscript.org).

If you have a fix or an improvement to the models we are happy to accept it. Code contributions and 
fixes are submitted through [pull requests]() on GitHub. 

Simply fork this repository, editor your fork and [start a pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 



:::{only} draft
::::{dropdown} Release checklist

1. Update `AMMR.version.any`.

   - Update with the new version numbers

   - Fill the `ANYBODY_HASH_BODY`. The new value can be found in `Main.HumanModel.Config.HashBodyModel`.

2. Update any  AMS version number in `Docs/conf.py` (only used when building locally)

3. Create new version of AMMR on Zenodo (<https://zenodo.org/record/3404750).

   - Click `New version` button

   - Fill the neccessary fields. Authors are those who contributed since last Release

   - Note the draft DOI which zenodo reserves

   - Save the draft but do **not** publish it.

4. Clean up, and update `Docs/changelog.rst`

   - Prof read and check that all changes are documented.

   - Add Zenodo DOI url to the new release, and fill the date

5. Check that the docs can build, and that the tests pass.

6. Merge the branch and add a git tag.

7. Upload ammr zip file to Zenodo

   - Either use the AMMR zip file created by the AMS build. This  (it con or create a

     **released zip file by running:**

     ```
     cd Docs
     make release
     mv release.zip ammr-X.Y.Z.zip
     ```

     This creates a zip file with the built documentation.

   - Edit the draft Zenodo release to upload a zip file with AMMR.

::::
:::









