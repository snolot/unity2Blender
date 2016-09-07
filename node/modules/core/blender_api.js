var fs 		= require('fs');
var path 	= require('path');
var config	= require('config');

function executeCommand(_jsonCommand){
	
	var exec = require('child_process').exec;

	var child = exec(config.get('blender.path') + ' ' + __base + 'public/blender/watch/watch.blend -b -P ' + __base + 'public/blender/watch/watch.py -- public/blender/watch/test '+_jsonCommand.hours+' '+_jsonCommand.minutes);

	child.stdout.on('data', function(chunk) {
	  console.log(chunk.toString());
	});

	// or if you want to send output elsewhere
	//child.stdout.pipe(dest);
}

module.exports = function(app){
	console.log('module is initialized.');

	app.post('/render', function(req, res){
		console.log('/render route called.');
		console.log(req.body);

		executeCommand(req.body);

		res.send('Render route called');
	});
}
