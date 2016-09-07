var express = require('express');
var config 	= require('config');
var path 	= require('path');
var fs 		= require('fs');
var _ 		= require('lodash');

global.__base = __dirname + '/';

var app 		= express();
var bodyParser 	= require('body-parser');

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

process.env.APP_VERSION = require('./package.json').version;

if (!process.env.NODE_ENV) {
    process.env.NODE_ENV = "home"; // local development environment
}

app.get('/', function(req, res){
  	res.send('Welcome to unity2blender api v'+process.env.APP_VERSION);
});

function loadModules(){
	
	var pathExists = function(){
		try {
	        var stat = fs.statSync(filepath);
	        return stat.isFile() || stat.isDirectory()
	    } catch (e) {
	        return false
	    }
	}

	var modules = config.get('modules');
	var modDir 	= __base + 'modules/';

	_.each(modules).forEach(function(module){
		if(module.enabled){
			console.log('try to load module: '+module.name);
			
			var mod = require(modDir+module.name)(app);
		}
	});
}

loadModules();

app.listen(3000);