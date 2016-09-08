var fs 		= require('fs');
var path 	= require('path');
var config	= require('config');

function executeCommand(_jsonCommand){
	
	var str = '"hours","minutes","x","y","z","eulerX","eulerY","eulerZ"\n';
	str  += _jsonCommand.hours+","+_jsonCommand.minutes+",";
	str += _jsonCommand.cam.x + "," + _jsonCommand.cam.y + "," + _jsonCommand.cam.z + ",";
	str += _jsonCommand.cam.eulerX + "," + _jsonCommand.cam.eulerY + "," + _jsonCommand.cam.eulerZ;

	var csvPath = __base + 'public/blender/watch/watch.csv';
	console.log(csvPath);

	fs.writeFile(csvPath, str, function(err) {
	    if(err) {
	        return console.log(err);
	    }

	    console.log("The file was saved!");

	    var exec 	= require('child_process').exec;
		var child 	= exec(config.get('blender.path') + ' ' + __base + 'public/blender/watch/watch.blend -b -P ' + __base + 'public/blender/watch/watch.py -- ' + __base + 'public/blender/watch/test '+ csvPath);

		child.stdout.on('data', function(chunk) {
		  console.log(chunk.toString());
		});
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
