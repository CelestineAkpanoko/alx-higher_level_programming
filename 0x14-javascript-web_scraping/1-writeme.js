#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 2) {
  fs.writeFile(process.argv[2], process.argv[3], (err, data) => {
    if (!err) {
      console.log(data.toString('utf-8'));
    } else {
      console.log(err);
    }
  });
}
