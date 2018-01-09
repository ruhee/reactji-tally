var PythonShell = require('python-shell');
PythonShell.run('scripts/run.py', function (err, results) {
  if (err) {
    console.log(err);
  } else {
    console.log(results)
  }
});
