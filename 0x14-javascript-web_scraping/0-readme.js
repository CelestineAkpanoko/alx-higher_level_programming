#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (err, data) => {
    if (!err) {
      console.log(data.toString('utf-8'));
    } else {
      console.log(err);
    }
  });
}
