# io.open(filename \[, mode])



This function opens a file, in the mode specified in the string `mode`. It returns a new file handle, or, in case of errors, **nil** plus an error message.

The `mode` string can be any of the following:

* **"`r`":** read mode (the default)
* **"`w`":** write mode
* **"`a`":** append mode
