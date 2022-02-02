#!/usr/bin/node

const re = require('request');

if (process.argv.length > 2) {
	re.get(process.argv[2])
	.on('response', function(response) {
		console.log('code: ', response.statusCode)
	})
}
