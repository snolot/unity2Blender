var fs 		= require('fs');
var path 	= require('path');

module.exports = function(app){
	console.log('module is initialized.');

	app.get('/render', function(req, res){
		res.send('Render route called');
	});
}
