CONTRIBUTING
====

Contributing guidelines and helpful stuff for this project


git
----

There are loads of git guidelines online that are better than this, but in short your workflow will be:
 - check out the main branch: `git checkout main`
 - bring in new changes: `git pull`
 - create a new branch: `git checkout -b feature/my_new_cool_branch`
 - make whatever code changes on this branch, committing regularly\*
 - remember to add tests if appropriate!
 - push your changes with `git push` (its best to do this regularly)
 - go to GitHub, create a Pull Request
 - someone else will review your code and add comments/approve it
 - once approved, your changes will be merged into the `main` branch

\*Committing your changes:
 - run `git status` to see what files have changed since the last commit
 - add your files to git's staging area: `git add myFile.py`myOtherFile.py
 - commit your changes: `git commit`

When you commit, add a helpful message (e.g. "implement the sort function"); not "made some changes" or "stuff"

other useful git commands:
 - `git diff` see what changes have been made since the last commit. This only tracks changes to files that have already been committed, so doesn't show changes to new files!
 - `git diff --name-only` see what files have been changed since the last commit
 - `git log` view the list of commits on the current branch, newest first
 - `git branch` see what branch you're currently on
 - `git stash` temporarily undo changes you've made since the last commit. Undo this with `git stash pop`; throw them away permanently with `git stash drop`


Formatting
----

Formatting is enforced using `black`; this gets checked on every commit that gets pushed to the remote and also for every
pull request.

To format your code, run `black myFile.py` where `myFile.py` is the name of the file you have been editing

tip: to automatically all files that have been changed in git since your last commit, run

```
git diff --name-only -- '*.py' |xargs black

```
(this won't automatically format brand new files though).


Tests
----

Automated tests are good for a number of reasons; mostly because they check your code does what you expect, but they
also force you to write modular, scaleable etc. code. A unit test should test a single piece of functionality, e.g. a
single calculation or bit of logic- this means all your logic/calculations should be split up into individual functions
with individual tests.

Since we're using pytest the tests should all be functions beginning with `test_`: e.g.

```
test_my_fcn(x):
"""
Check that my_fcn correctly returns the right thing, and that it raises an error if we pass it 0
"""
    assert my_fcn(2) == 4

    with pytest.raises(ValueError):
        my_fcn(0)

```
a guide to writing tests with pytest is online

Run all test tests in the test directory using `python -m pytest test/`. They also get run in the GitHub actions.


GitHub actions
----

The automated tests and a check that the formatting is right is performed every time you push your code.
This just checks that everything is in order and ready to be merged, so you're warned early if something isn't right.


