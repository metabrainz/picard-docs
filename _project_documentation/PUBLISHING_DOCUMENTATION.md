# Publishing the Documentation

Documentation versions are published as `v{major}.{minor}` only (based on the corresponding `v{major}.{minor}` branch) and do not include the `micro` component of the version number that is added for maintenance or "patch" versions. The `main` branch is published as the `latest` version, which may include changes or functionality from a pre-release version of Picard. The `next_version` branch is used to collect changes prior to a `v{major}.{minor}` pre-release version of Picard being issued. Once this pre-release version of Picard version is made available, the `next_version` branch is merged into the `main` branch so that the documentation is published to the website as the `latest` version. A new `v{major}.{minor}` branch can also be created based on the `main` branch so that the documentation is also published to the website as the `v{major}.{minor}` version, although this is typically not done until the Picard `v{major}.{minor}` version is released as "final" rather than as a pre-release.

## Picard Development Phase

When development begins on a new `v{major}.{minor}` version of Picard, the `main` branch of the documentation repository is merged into the `next_version` branch to ensure that all previous changes are included, and to help reduce future merge conflicts.

During the development of this new version of Picard, any changes to the documentation such as new or modified options or functionality are collected in the `next_version` branch of the documentation repository. This branch is not published to the documentation website.

## Picard Pre-Release Testing Phase

When the new `v{major}.{minor}` pre-release (alpha, beta or release candidate) version of Picard is made available for testing, the `next_version` branch of the documentation is merged into the `main` branch so that the documentation is published to the website as the `latest` version. Any further documentation updates for this new version are added to the `main` branch. Optionally during this testing phase, the `next_version` branch can be updated so that it is synchronized with the `main` branch in preparation for the next new `v{major}.{minor}` version of Picard.

Optionally, a new `v{major}.{minor}` branch can also be created based on the `main` branch so that the documentation is also published to the website as the `v{major}.{minor}` version, although this is typically not done until the Picard `v{major}.{minor}` version is released as "final" rather than as a pre-release. Note that if this new `v{major}.{minor}` branch is created, any changes merged into the `main` branch should also be merged into the `v{major}.{minor}` branch once the changes are applicable to the (pre-release) version of Picard made publicly available.

## Post Picard Release

Once a `v{major}.{minor}` version of Picard has been released as "final", a new `v{major}.{minor}` branch should be created based on the `main` branch if this has not already been done during the pre-release testing phase. This ensures that the `v{major}.{minor}` version appears as an option on the documentation website. Once this branch has been created, any applicable changes (including translation updates) pushed to the `main` branch will also need to be merged into this `v{major}.{minor}` branch so that the website is properly updated.

Documentation changes for subsequent Picard "patches" or `micro` releases to a `v{major}.{minor}` version should be added to the `main` branch, and later merged into the applicable `v{major}.{minor}` branch once the Picard patch or `micro` version is released.

## Changes to Prior Releases

When a documentation change (including additional or modified translations) is made to a `v{major}.{minor}` version prior to the latest `v{major}.{minor}` version, the changes should be applied directly to the applicable `v{major}.{minor}` branch and **not** through the `main` branch. The reason for this is that the changes may not be applicable to the latest `v{major}.{minor}` version, which will typically be updated based on the `main` branch.

-----

## Notes

The system publishes documentation from the `main` branch (as "latest" version) and the `v{major}.{minor}` branches (as "v{major}.{minor}" versions) to the documentation website. Changes to these branches will automatically trigger a rebuild of the documentation.

When a new `v{major}.{minor}` branch is added, it will be automatically added as a new `v{major}.{minor}` version to the documentation website.

Branches other than `main` and those in the format `v{major}.{minor}` will not be published by default. This allows collecting future updates in branches such as the `next_version` branch.

To avoid potential problems, `v{major}.{minor}` tags should **not** be added to commits in the documentation repository.

Translations are managed using [Weblate](https://translations.metabrainz.org/projects/picard-docs/), which connects to the `main` branch. When documentation changes have been made to the `main` branch, the translations templates should be updated to ensure that the translators are working with the latest information.
