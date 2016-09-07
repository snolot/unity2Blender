var express = require('express');
var config = require('config');

console.log(config.get('blender.path'));
