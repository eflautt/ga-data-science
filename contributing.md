# Contributing

### Pull Requests

All PRs should be submitted from a feature branch on your local fork, straight to *generalassembly/wdi/master*.

Before submitting a pull request, please make sure your local feature branch is up to date with generalassembly/wdi/master:

    $ git remote add upstream git@github.com:generalassembly-studio/dat-curriculum
    $ git fetch --all
    $ git checkout -b my-feature-branch upstream/master

### Lesson, project, and homework branches

If you're submitting a new _lesson_, _lab_, or _homework_ resource, **create a feature branch** for each individual resource.

Lesson branch naming should follow the same naming style & convention we use for folders. For example:

```
$ git checkout master
On branch master
nothing to commit, working directory clean

$ git checkout -b intro-to-relational-data-modeling
Switched to a new branch intro-to-relational-data-modeling
```

If a lesson/lab/homework both have the exact same name, just denote which with `-lesson` or `-lab`.

```
$ git checkout -b exploratory-data-analysis-lesson

- - or - -

$ git checkout -b exploratory-data-analysis-lesson
```

If submitting a new resource, please also make sure the resources:

- follow our [styleguide](templates/styleguide.md), with appropriate YAML frontmatter data
- are in the standard [lesson](templates/template-lesson-readme.md) and [project](templates/template-project-readme.md) templates
