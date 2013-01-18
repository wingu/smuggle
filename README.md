smuggle allows you to import a python module from a specific path, without making a permananent modification to sys.path.  (It imports something secretly... by smuggling... is what we're saying)

### Why would you want to do such a thing?

Because sometimes, just sometimes, as part of your deploy/testing/etc, you're going to have separate chunks of code you need to pull together, but full modifications to sys.path would result in painful conflicts.

### Is this a sign that your code isn't perfectly organized?

Yes.

### Do such things happen in the Real World, and thus justify the occasional odd hack?

Also, yes.
