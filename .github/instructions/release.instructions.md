---
description: Instructions needed to prepare a release version of the AnyBody Managed Model Repository (AMMR)
---

# Release Instructions
This document describes the steps needed to prepare a release version of the AnyBody Managed Model Repository (AMMR). The instructions are intended for maintainers of the repository, and should be followed carefully to ensure that the release process goes smoothly.

## Step 1: Update the Version Number
The first step in preparing a release is to update the version number in the `AMMR.version.any` file. This file is located in the root directory of the repository, and contains the version number of the AMMR. The version number should be updated according to the [Semantic Versioning](https://semver.org/) guidelines. There is both a `AMMR_VERSION` string variable of the version and a `AMMR_VERSION_MAJOR`, `AMMR_VERSION_MINOR`, and `AMMR_VERSION_PATCH` integer variables. All of these should be updated to reflect the new version number. For example, if the current version is `1.2.3` and the new version is `1.3.0`, the `AMMR.version.any` file should be updated as follows:

```anyscript
#define AMMR_VERSION = "1.3.0"
#define AMMR_VERSION_MAJOR = 1
#define AMMR_VERSION_MINOR = 3
#define AMMR_VERSION_PATCH = 0
```

## Step 2: Update the Changelog
The next step is to update the `CHANGELOG.md` file with the changes that have been made since the last release. Each release should have a title which is the version number of the release and the release date in the format `YYYY-MM-DD`. The changelog should include a summary of the changes. We use four sections in the changelog: Added, Changed, Removed, and Fixed. Each section should contain a list of changes that fall under that category.
Each section should prepare a Zenodo badge to the release. The link is the first item in the section and should be formatted as follows:
```
[![Zenodo Link](https://zenodo.org/badge/DOI/10.5281/zenodo.<DOI_NUMBER>.svg)](https://doi.org/10.5281/zenodo.<DOI_NUMBER>)
```
Where `<DOI_NUMBER>` is the DOI number assigned to the release on Zenodo.
```
Each section should also include a link to the AnyBody download page for the AMS release associated with the AMMR release. The link should be formatted as follows:
```[![AnyBody link](https://img.shields.io/badge/Included_with_AnyBody-<ANYBODY_VERSION>-yellowgreen)](https://www.anybodytech.com/resources/customer-downloads/)
```
Where `<ANYBODY_VERSION>` is the version of AnyBody that includes the AMMR release.

## Step 3: Update the AnyBody used in CI Pipelines
If the new release of the AMMR requires a new version of AnyBody, the AnyBody version used in the CI pipelines should also be updated. This can be done by updating the anybodycon dependency in the feature.anybodycon.target.win-64.dependencies entry in the `pixi.toml` file. The version number should be updated to the version of AnyBody that includes the AMMR release.

## Step 3: Create a Release Tag
After updating the version number and the changelog, the next step is to create a release tag in the Git repository. This can be done using the following command:
```git tag -a ams.<VERSION_NUMBER> -m "Release version <VERSION_NUMBER>"
```
Where `<VERSION_NUMBER>` is the version number of the AMS release associated with the AMMR release. After creating the tag, it should be pushed to the remote repository using the following command:
```git push origin ams.<VERSION_NUMBER>
```

## Step 4: Create a Release on GitHub
The final step is to create a release on GitHub. This can be done by navigating to the "Releases" section of the repository on GitHub and clicking on the "Draft a new release" button. The release should be titled with the version number and the release date, and the description should include the summary of changes from the changelog. The release should also be tagged with the same version number as the Git tag created in the previous step. Once the release is ready, it can be published by clicking the "Publish release" button.

## Conclusion
Following these steps will ensure that the release process for the AMMR goes smoothly and that the release is properly documented and tagged. It is important to follow these instructions carefully to maintain the integrity of the repository and to provide clear information about the changes included in each release. If you have any questions or need further assistance, please reach out to the maintainers of the repository.
